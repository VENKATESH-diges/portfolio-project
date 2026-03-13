from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import random

def Enter_page(request):
    if request.method == "POST":
        username=request.POST.get("name")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None :
            login(request,user)
            return redirect('home')
 
        else:
            messages.error(request,"Invalid username or password")
        return redirect('login_enterpage')
    return render(request,'enter.html')

        
def home(request):
    return render (request,"home.html")
    
def forget_p(request):
     if request.method == 'POST':
         email=request.POST.get('email')
         if not email :
             
             return render(request,'password_reset.html',{
                 "error": "Please enter your email"
             })
        
         try:
            user = User.objects.filter(email=email).first()
         except User.DoesNotExist:
            messages.error(request,"Email not registered")
            return render(request,'password_reset.html',{
                "error": "Email not registered"
            })

         subjust=" portfolio App Your Forget paswword Otp"
         otp=random.randint(10000,99999)
         send_person=settings.EMAIL_HOST_USER
         reciver=[email]
         send_mail(
             subjust,
             f'your Otp:{otp} check it up carefuly' ,
             send_person,
             reciver)
         return HttpResponse("sucessfuly send opt")

          
             
     else :
         return render(request,"password_reset.html")


     
def log_out(request):
    logout(request)
    return redirect('login_enterpage')

    
    
