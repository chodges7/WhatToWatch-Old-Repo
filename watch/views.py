from django.contrib.auth import login, logout
from django.shortcuts import render , redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from imdb import IMDb

from . import models
from . import forms

@login_required(login_url="/login/")
def blank(request):
    return redirect("/home/")

@login_required(login_url="/login/")
def home(request):
    # Get top 50 movies
    moviesData = IMDb()
    top = moviesData.get_top250_movies()

    context = {
        "name":'LineUp Login Signup',
        "movies":top,
    }
    return render(request,'home.html', context=context)

@login_required(login_url="/login/")
def profile_view(request):
    prof = models.Profile.objects.get(profile_user=request.user)
    welc = "Welcome to your profile page: "
    welc += prof.profile_fname + " " + prof.profile_lname

    # FORMS for this page
    if request.method == "POST":
        form = forms.BioForm(request.POST)
        if form.is_valid():
            prof.profile_bio = form.cleaned_data["profile_bio"]
            prof.save()
            form = forms.BioForm()
            return redirect('/profilePage/')
    else:
        form = forms.BioForm()
    if request.method == "POST" and not form.is_valid():
        form_picture = forms.PictureForm(request.POST, request.FILES)
        if form_picture.is_valid():
            prof.profile_image = form_picture.cleaned_data["profile_image"]
            prof.save()
            form_picture = forms.PictureForm()
            return redirect('/profilePage/')
    else:
        form_picture = forms.PictureForm()

    context = {
        "body":welc,
        "form":form,
        "form_picture":form_picture,
        "title":"Profile Page",
        "bio":prof.profile_bio,
        "profile_picture":prof.profile_image,
    }
    return render(request, "profile_page.html", context=context)

def login_view(request):
    # Authentication works
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/home/')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'name':'LineUp login Signup','form':form})

@login_required(login_url="/login/")
def logout_view(request):
    logout(request)
    return redirect("/home/")

def signup(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
        "title":"Registering User",
        }
    return render(request, "signup.html", context=context)
