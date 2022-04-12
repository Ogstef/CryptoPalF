import requests
from django.contrib.auth import login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Currency
from .forms import NewUserForm, UserForm, ProfileForm
from django.contrib import messages
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def rate(request):
    return render(request, 'rate.html', {

        "v_currencies": Currency.objects.all()
    })


def search(request):
    if request.method == "POST":
        searched = request.POST["q"]  # sometimes need parentheis
        smatch = Currency.objects.filter(
            description__contains=searched) | Currency.objects.filter(
                name__contains=searched)
        return render(request, "search_results.html", {
            "searched": searched,
            "schedules": smatch
        })
    else:
        return render(request, "search_results.html", {})


def contact(request):
    return render(request, "contact.html")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("website:index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("website:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("website:index")


def profpage(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile was successfully updated!')
        elif profile_form.is_valid():
            profile_form.save()
        else:
            messages.error(request, 'Unable to complete request')
        return redirect("website:profpage")
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request=request, template_name="profile.html", context={"user": request.user,
                                                                          "user_form": user_form,
                                                                          "profile_form": profile_form})
