import os
from email.mime.image import MIMEImage

from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            subject = 'Share With Care (SWC)'
            email = user.email
            message = f'Greetings {user.username}! You have successfully logged into ShareWithCare.com. Enjoy Shopping!'
            auth.login(request, user)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
            msg = EmailMultiAlternatives(
                subject,
                message,
                from_email=email_from,
                to=[recipient_list]
            )
            msg.mixed_subtype = 'related'

            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        role = request.POST['role']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();

                subject = 'Share With Care (SWC)'
                if role == 'Vendor':
                    message = f'Greetings {user.username}! Thank You for registering into ShareWithCare.com as a/an {role}.\nYou now have privileges such as Adding/Viewing Raw Products, End Products.\nLogin to localhost:8000/accounts/login with your credentials to avail the privileges.\n'
                elif role == 'Customer':
                    message = f'Greetings {user.first_name}! Thank You for registering into ShareWithCare.com as a new user.\nYou can now Login into localhost:8000/accounts/login with your credentials {user.username} as your username.\n'
                else:
                    message = f'Greetings {user.username}!You are now an Admin for ShareWithCare.com.\nYou now have privileges such as CRUD of Raw Products, End Products.\nLogin to localhost:8000/admin with your credentials to avail the privileges.\n'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, email_from, recipient_list)
                msg = EmailMultiAlternatives(
                    subject,
                    message,
                    from_email=email_from,
                    to=[recipient_list]
                )

                return redirect('login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')
        return redirect('/')
        
    else:
        return render(request,'register.html')




def logout(request):
    auth.logout(request)
    return redirect('/')       