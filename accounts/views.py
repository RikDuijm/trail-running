from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required 
from accounts.forms import UserLoginForm

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