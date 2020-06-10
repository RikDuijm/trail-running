from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required 
from django.db.models import Q  # for searches on several fields of model
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm, ProfilePostForm, ContactProfileForm
from .models import UserProfile, ProfilePost, ContactUser


def index(request):
    """View that returns the index / homepage"""  
    return render(request, "index.html")

def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        # User is already registered, so no point to be on registration page.
        return redirect(reverse('index')) 

    if request.method == "POST":
        # Check of the method is post. If so instantiate the registration and profile forms, using the values of the request post method.
        registration_form = UserRegistrationForm(request.POST)  
        # request.Files to upload profile pic.
        profile_form = UserProfileForm(request.POST, request.FILES)  
        # If registration form is valid, safe it
        if registration_form.is_valid() and profile_form.is_valid(): 
            user = registration_form.save()
            # To add the user to this profile, use commit=False to not safe the profile to database right away.
            profile = profile_form.save(commit=False)   
            # Refers to models.user and makes sure that one user only has one profile
            profile.user = user                         
            profile.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)                          
                # Send message to user that he has registered successfully or not.
                messages.success(request, "You have successfully registered and are logged in.")
                return redirect(reverse('profile'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        # Else statement in case it's a get method. An empty registration form is instantiated.
        registration_form = UserRegistrationForm()          
        profile_form = UserProfileForm()
    
    return render(request, 'registration.html', {
        "registration_form": registration_form, "profile_form": profile_form})    
    

def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST) 
        # if request method is equal to POST then create an instance of the user login form, so a new login form will be created with the data posted from the form on the UI 
        # check if data is valid.
        if login_form.is_valid():  
            # this will authenticate the user, whether or not this user has provided the username and password
            user = auth.authenticate(username=request.POST['username'],  
                                    password=request.POST['password'])
            if user:
                # Then the authenticate function will return a user object. If there's a user,  we'll log him in.
                auth.login(user=user, request=request) 
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect.")
    else:
        login_form = UserLoginForm() 
    return render(request, 'login.html', {'login_form': login_form})


@login_required
# required to only allow access to the logout page if user is authenticated. 
# Django automatically redirects to login page if logged out user tries to enter logout page by url
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out.")
    return redirect(reverse('index'))


@login_required
def all_users(request):
    """
    View returns a list of Profiles that were published and render them 
    to the 'allprofiles.html' template
    """
    # order users by last name
    users = UserProfile.objects.all().order_by('last_name')
    return render(request, "allusers.html", {'users': users})   


@login_required
def user_profile(request, pk=None):
    """The user's profile page"""
    # user is indentified by his email
    user = User.objects.get(email=request.user.email)
    # show profileposts, fist identifying the user and then ordering by date, new first
    profileposts = ProfilePost.objects.filter(user=request.user).filter(published_date__lte=timezone.now()
        ).order_by('-published_date').all()
    # show messages to user, ordering by date, new first. In template an if statement makes sure only the messages of the logged-in user show
    contactuserposts = ContactUser.objects.all().filter(date__lte=timezone.now()
        ).order_by('-date').all()  
    return render(request, 'profile.html', {"profile": user, 'profileposts': profileposts, 'contactuserposts': contactuserposts})   


@login_required
def profile_post(request, pk=None):
    """
    Create a view that allows user to add new info on his profile
    """
    user = User.objects.get(email=request.user.email)
    if request.user.is_authenticated:  
        if request.method == 'POST':
            profile_post_form = ProfilePostForm(request.POST, request.FILES)
            if profile_post_form.is_valid():
                profilepost = profile_post_form.save(commit=False)
                profilepost.user = request.user
                profilepost.save()
                messages.success(request, 'Your post has been published!')
                return redirect(reverse('profile'))
        else:
            profile_post_form = ProfilePostForm()
    else:
        return redirect('login') 
    return render(request, 'newprofilepost.html', {'profile_post_form': profile_post_form, 'profile': user})


@login_required
def contact_user(request, pk=None):
    """
    Create a view that allows the logged-in user to contact another user
    """
    # another way of checking if user is logged-in
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'GET':
            # identifying the sender and recipient of the message
            sender = User.objects.get(email=request.user.email)
            data = {'recipient': get_object_or_404(User, pk=pk)}
            contact_profile_form = ContactProfileForm(initial=data)
        else:
            contact_profile_form = ContactProfileForm(request.POST, request.FILES)
            if contact_profile_form.is_valid():
                sender = User.objects.get(email=request.user.email)
                contactuserpost = contact_profile_form.save(commit=False)
                contactuserpost.sender = request.user
                messages.success(request, 'Your message has been successfully sent!')
                contactuserpost.save()              
                return redirect(reverse('all_users'))
            else:
                contact_profile_form = ContactProfileForm()
    return render(request, 'contactuserpost.html', {'contact_profile_form': contact_profile_form})


@login_required
def edit_profile(request, pk=None):
    """
    Create a view that allows user to edit his profile details
    """
    profiledetails = UserProfile.objects.filter(user=request.user).first()
    if UserProfile.objects.filter(user=request.user or request.user.is_superuser):

        if request.method == "POST":
            profile_details_form = UserProfileForm(request.POST, request.FILES, instance=profiledetails)
            if profile_details_form.is_valid():
                profiledetails = profile_details_form.save()
                messages.success(request, 'Your profile has been updated!')
                return redirect(user_profile)
        else:
            profile_details_form = UserProfileForm(instance=profiledetails)
    else:
        return HttpResponseForbidden()
    
    return render(request, 'newprofiledetails.html', {'profile_details_form': profile_details_form})


@login_required
def edit_profile_post(request, pk=None):
    """
    Create a view that allows user or admin to edit info on the profile
    """
    profilepost = get_object_or_404(ProfilePost, pk=pk)      
    if (request.user == profilepost.user or
            request.user.is_superuser):
        if request.method == "POST":
            profile_post_form = ProfilePostForm(request.POST, request.FILES, instance=profilepost)
            if profile_post_form.is_valid():
                profilepost = profile_post_form.save()
                messages.success(request, 'Your post has been updated!')                
                return redirect(reverse('profile'))
        else:
            profile_post_form = ProfilePostForm(instance=profilepost)
    else:
        return HttpResponseForbidden()

    return render(request, 'newprofilepost.html', {'profile_post_form': profile_post_form})


@login_required    
def delete_profile_details(request, pk=None):
    """
    Create a view that allows user or admin to delete the profile.
    """
    user = User.objects.get(email=request.user.email)
    profiledetails = UserProfile.objects.filter(user=request.user).first()

    if UserProfile.objects.filter(user=request.user or request.user.is_superuser):
        if request.method == "POST":
            profiledetails.delete()
            user.delete()
            return redirect(deleted_user)
    return render(request, "profiledetailsdelete.html", {'profiledetails': profiledetails})


def deleted_user(request):
    """Log the user out after profile has been deleted"""
    auth.logout(request)
    messages.success(request, "Your profile has been deleted. Please contact us if you want to undo this.")
    return redirect(reverse('index'))
    
@login_required
def delete_profile_post(request, pk=None):
    """
    Create a view that allows user or admin to delete
    information on the profile.
    """
    user = User.objects.get(email=request.user.email)
    profileposts = ProfilePost.objects.filter(user=request.user)
    profileposts = ProfilePost.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date').all()
    contactuserposts = ContactUser.objects.all()  
    profilepost = get_object_or_404(ProfilePost, pk=pk)
    if (request.user == profilepost.user or
            request.user.is_superuser):
        if request.method == "POST":
            profilepost.delete()
            messages.success(request, 'This information has been successfully deleted.')
            return render(request, 'profile.html', {'profileposts': profileposts, 'profile': user, 'contactuserposts': contactuserposts})
    return render(request, "profilepostdelete.html", {'profilepost': profilepost})


@login_required
def delete_personal_message(request, pk=None):
    """
    Create a view that allows user to delete a personal message to him / her
    """
    user = User.objects.get(email=request.user.email)
    contactuserposts = ContactUser.objects.all()
    contactuserpost = get_object_or_404(ContactUser, pk=pk)
    if request.method == "POST":
        contactuserpost.delete()
        messages.success(request, 'This message has been successfully deleted.')
        return redirect(user_profile)
    return render(request, "personalmessagedelete.html", {'contactuserposts': contactuserposts})


@login_required
def author_profile(request, pk):
    """The profile of the author of the blogpost"""
    author = get_object_or_404(User, pk=pk)
    profileposts = ProfilePost.objects.filter(user=author).filter(published_date__lte=timezone.now()
         ).order_by('-published_date').all()
    return render(request, 'profile.html', {"profile": author, 'profileposts': profileposts})
    

@login_required
def user_profile_page(request, pk=None):
    """Create a view that will link to the profile of a user"""
    userprofile = get_object_or_404(User, pk=pk)
    profileposts = ProfilePost.objects.filter(user=userprofile).filter(published_date__lte=timezone.now()
         ).order_by('-published_date').all() 
    return render(request, 'profile.html', {"profile": userprofile, 'profileposts': profileposts})


def search_user_first_name(request):
    """Create a view that will filter the profiles based on
    first name, last name and location"""
    q1 = request.GET.get('q1')
    users = UserProfile.objects.filter(
        Q(first_name__icontains=q1))
    return render(request, "allusers.html", {"users": users})    


def search_user_last_name(request):
    """Create a view that will filter the profiles based on
    first name, last name and location"""
    q2 = request.GET.get('q2')
    users = UserProfile.objects.filter(
        Q(last_name__icontains=q2))
    return render(request, "allusers.html", {"users": users})    


def search_user_location(request):
    """Create a view that will filter the profiles based on
    first name, last name and location"""
    q3 = request.GET.get('q3')
    users = UserProfile.objects.filter(
        Q(location__icontains=q3))
    return render(request, "allusers.html", {"users": users})   