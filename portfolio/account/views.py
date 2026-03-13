from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail 


def signup(request):
    if request.method=="POST":
        username=request.POST.get('Username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('ps1')
        pass2=request.POST.get('ps2')

        if User.objects.filter(username=username).exists():
            messages.error(request,"User sign in already exist")
            return redirect("sign_in")

        if pass1 != pass2 :
             messages.error(request,"password is does not match")
             return redirect("sign_in")
        else:
             user=User.objects.create_user(
                username=username,
                first_name=fname,
                last_name=lname,
                email=email,
                password=pass1
            )
             subject="Welcome to Portfolio App"
             message = f"""
                    Hi {fname},

                    Thank you for signing up to Portfolio App!

                    We are excited to have you onboard 

                    i give you one opportunity guys

                    Regards,
                    Portfolio 
                    """
    
             from_mail= settings.EMAIL_HOST_USER
             reciver=[email]
            #  send_mail(subject,message,from_mail,reciver)
            #  messages.success(request,"sign in sucessfuly plase loging")
             return redirect('login_enterpage',)
        
            
    else:
        return render(request,"siging.html")


