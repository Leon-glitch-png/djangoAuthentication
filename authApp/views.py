from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    CustomPasswordResetForm,
)
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    

        

def home(request):

    return render(request, "logged_in.html")


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = CustomUserCreationForm()

    return render(request, "registration/register.html", {"form": form})


def login_view(request):
    
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                context = {"message": "Login successful", "is_success": True}
                login(request, user)
                return redirect("home")
            
        


    else:
        form = CustomAuthenticationForm()

    return render(
        request, "registration/login.html", {"form": form,}
    )


# views_debug.py


def debug_template(request):
    return render(request, "registration/reset_done.html", {})



