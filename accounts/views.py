from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, ProfileIntroductionForm

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

def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})        

def profile_introduction(request):
    if request.method == 'POST':
        profile_introduction_form = ProfileIntroductionForm(request.POST)
        if profile_introduction_form.is_valid():
            profile_introduction_form.save()
            return render(request, 'profile.html')
    else:
        profile_introduction_form = ProfileIntroductionForm()
    return render(request, 'profile.html', {
        "profile_introduction_form": profile_introduction_form
    })