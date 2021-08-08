from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def booking(request):

    return render(request, "appoint.html")
        #
        # if request.method=="POST":
        #
        #     name = request.POST("name")
        #     email = request.POST("email")
        #     date = request.POST("date")
        #     message =request.POST("message")
        # else:
        #     return render(request,"appo.html")






