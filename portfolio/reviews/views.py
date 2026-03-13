from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Reviewers
from django.contrib.auth.decorators import login_required

@login_required
def Reviews_page(request):
    if request.method == "POST":
        title= request.POST.get("title")
        description=request.POST.get("description")

        Reviewers.objects.create(

        user=request.user,
        title=title,
        description=description
        )
        return render (request,"reviewsubmit.html")
    else:
        return render (request,"reviews.html")
     
def review_submit(request):
    return render(request,"reviewsubmit.html")

def reviews_all(request):

    allreviews= Reviewers.objects.all().order_by("-create_at")

    return render (request,"reviewsall.html",{"reviews":allreviews})

     