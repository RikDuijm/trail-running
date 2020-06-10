from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.models import User

def emailView(request):
    """
    View that a logged in can use to send an email to TrailRunning
    """
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'GET':
            user = User.objects.get(username=request.user.username)
            # The user.email is filled in by default and the receiving
            data = {'from_email': user.email}
            form = ContactForm(initial=data)
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                # If the ContactForm is filled in valid the email is send.
                subject = form.cleaned_data['subject']
                from_email = form.cleaned_data['from_email']
                message = form.cleaned_data['message']
                try:
                    send_mail(subject + " - " + from_email,
                              message,
                              from_email,
                              ['online.onderscheiden@gmail.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                # # After the email is send successfully the user is send to the
                # homepage and sees this message.    
                messages.success(request,
                                 "Thank you for you message! \
                                 We'll get back to you soon.")
                return redirect(reverse('index'))
        return render(request, "contact.html", {'form': form})