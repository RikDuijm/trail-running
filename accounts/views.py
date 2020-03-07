from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm, ProfilePostForm, ContactProfileForm
from .models import UserProfile, ProfilePost

def index(request):
    """View that returns the index / homepage"""  
    return render(request, "index.html")
    
@login_required
# required to only allow access to the logout page if user is authenticated; Django automatically redirects to login page if logged out user tries to enter logout page by url
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out.")
    return redirect(reverse('index'))

def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST) 
        # if request method is equal to POST then create an instance of the user login form, so a new login form will be created with the data posted from the form on the UI 
        if login_form.is_valid(): #check if data is valid, this is a method. 
            user = auth.authenticate(username=request.POST['username'], # this will authenticate the user, whether or not this user has provided the username and password 
                                    password=request.POST['password'])
            if user:
                auth.login(user=user, request=request) # Then our authenticate function will return a user object so if we have a user then we'll log him in.
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect.")
    else:
        login_form = UserLoginForm() # otherwise we're just going to create an empty object 
    return render(request, 'login.html', {'login_form': login_form})

def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index')) # User is already registered, so no point to be on registration page.

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST) # Check of the method is post. If so instantiate the registration and profile forms, using the values of the request post method. 
        profile_form = UserProfileForm(request.POST, request.FILES)  # request.Files to upload profile pic.

        if registration_form.is_valid() and profile_form.is_valid(): # If registration form is valid, safe it
            user = registration_form.save()

            profile = profile_form.save(commit=False)   # To add the user to this profile, commit=False to not safe the profile to database right away.
            profile.user = user                         # Refers to models.user and makes sure that one user only has one profile

            profile.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)                          # Send message to user that he has registered successfully or not.
                messages.success(request, "You have successfully registered and are logged in.")
                return redirect(reverse('profile'))
            
            else:
                messages.error(request, "Unable to register your account at this time")
    
    else:
        registration_form = UserRegistrationForm()          # Put an else statement in case it's a get method. Then we'll just instantiate an empty registration form.
        profile_form = UserProfileForm()
    
    return render(request, 'registration.html', {
        "registration_form": registration_form, "profile_form": profile_form})


def all_users(request):
    """
    Create a view that will return a list
    of Profiles that were published and render them 
    to the 'allprofiles.html' template
    """
    user = User.objects.get(email=request.user.email)
    users = User.objects.all()
    return render(request, "allusers.html", {'users': users}, {"user": user})   
   

def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
#    return redirect(reverse('profile', {"profile": user}))
    profileposts = ProfilePost.objects.filter(user=request.user)
    return render(request, 'profile.html', {"profile": user, 'profileposts': profileposts})     

# # https://stackoverflow.com/questions/25615753/attributeerror-str-object-has-no-attribute-fields-using-django-non-rel-on-g


def profile_post(request, pk=None):
    """
    Create a view that allows user to add new info on his profile
    """
    user = User.objects.get(email=request.user.email)
    if request.user.is_authenticated:  # Is this necessary? User is already authenticated to be able to get to this point.
        if request.method == 'POST':
            profile_post_form = ProfilePostForm(request.POST, request.FILES)
            if profile_post_form.is_valid():
                profilepost = profile_post_form.save(commit=False)
                # profilepost.user = User.objects.get(email=request.user.email)  # !!!!
                profilepost.user = request.user  # this fixed the line above
                profilepost.save()
                # return redirect(user_profile_page)
                return redirect(reverse('profile'))
        else:
            profile_post_form = ProfilePostForm()
    else:
        return redirect('login') 
    return render(request, 'newprofilepost.html', {'profile_post_form': profile_post_form, 'profile': user})

def contact_user(request, pk=None):
    """
    Create a view that allows the logged-in user to contact another user
    """
    user = User.objects.get(email=request.user.email)
    if request.user.is_authenticated:  
        if request.method == 'POST':
            contact_profile_form = ContactProfileForm(request.POST, request.FILES)
            if contact_profile_form.is_valid():
                contactuserpost = contact_profile_form.save(commit=False)
                contactuserpost.user = request.user 
                contactuserpost.save()              # this must be saved at profile of the user who is being contacted. 
                # return redirect(user_profile_page)
                return redirect(reverse('profile'))
        else:
            contact_profile_form = ContactProfileForm()
    else:
        return redirect('login') 
    return render(request, 'contactuserpost.html', {'contact_profile_form': contact_profile_form, 'profile': user})


def edit_profile(request, pk=None):
    """
    Create a view that allows user to edit his profile details
    """
    profiledetails = UserProfile.objects.filter(user=request.user).first()
    if UserProfile.objects.filter(user=request.user or request.user.is_superuser):
    # if (request.user == profiledetails.user or
    #         request.user.is_superuser):
        if request.method == "POST":
            profile_details_form = UserProfileForm(request.POST, request.FILES, instance=profiledetails)
            if profile_details_form.is_valid():
                profiledetails = profile_details_form.save()
                return redirect(user_profile)
        else:
            profile_details_form = UserProfileForm(instance=profiledetails)
    else:
        return HttpResponseForbidden()
    
    return render(request, 'newprofiledetails.html', {'profile_details_form': profile_details_form})


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
                #return redirect(user_profile_page)
                return redirect(reverse('profile'))
        else:
            profile_post_form = ProfilePostForm(instance=profilepost)
    else:
        return HttpResponseForbidden()

    return render(request, 'newprofilepost.html', {'profile_post_form': profile_post_form})
    

def delete_profile_details(request, pk=None):
    """
    Create a view that allows user or admin to delete
    the profile details.
    """
    user = User.objects.get(email=request.user.email)
    profiledetails = UserProfile.objects.filter(user=request.user).first()

    if UserProfile.objects.filter(user=request.user or request.user.is_superuser):
        if request.method == "POST":
            profiledetails.delete()
            messages.success(request, 'This information has been successfully deleted.')
            return redirect(user_profile)
    return render(request, "profiledetailsdelete.html", {'profiledetails': profiledetails})


def delete_profile_post(request, pk=None):
    """
    Create a view that allows user or admin to delete
    information on the profile.
    """
    user = User.objects.get(email=request.user.email)
    profileposts = ProfilePost.objects.filter(user=request.user)
    profilepost = get_object_or_404(ProfilePost, pk=pk)
    if (request.user == profilepost.user or
            request.user.is_superuser):
        if request.method == "POST":
            profilepost.delete()
            messages.success(request, 'This informationhas been successfully deleted.')
            return render(request, 'profile.html', {'profileposts': profileposts, 'profile': user})
    return render(request, "profilepostdelete.html", {'profilepost': profilepost})


# def get_profile_posts(request):
#    """
#    Create a view that will return a list
#    of Posts that were published prior to 'now'
#    and render them to the 'blogposts.html' template
#    """
#    profileposts = ProfilePost.objects.filter(published_date__lte=timezone.now()
#        ).order_by('-published_date').all()
#    return render(request, "test.html", {'profileposts': profileposts})


def author_profile(request, pk):
    """The profile of the author of the blogpost"""
    author = get_object_or_404(User, pk=pk)
    profileposts = ProfilePost.objects.filter(user=author)
    # profileposts = ProfilePost.objects.filter(user=request.user)    
    return render(request, 'profile.html', {"profile": author, 'profileposts': profileposts})
    

def user_profile_page(request, pk=None):
    """Create a view that will link to the profile of a user"""
    userprofile = get_object_or_404(User, pk=pk)
    # userprofile = get_object_or_404(UserProfile, pk=pk)
    profileposts = ProfilePost.objects.filter(user=userprofile)
    return render(request, 'profile.html', {"profile": userprofile, 'profileposts': profileposts})
 