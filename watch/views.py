from django.contrib.auth import login, logout
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserM
from .forms import UserF
from django.contrib.auth import authenticate , login
def home(request):
    return render(request,'home.html',{'name':'LineUp Login Signup'})

def login_view(request):
    # Authentication works
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
          user = form.get_user()
          login(request, user)
          return redirect('/home')    
    else:    
        form = AuthenticationForm()
    return render(request,'login.html',{'name':'LineUp login Signup','form':form})

def signup(request):
    #TODO remove print statements
    print("Reached signup function")
    if request.method == 'POST':
        print("Reached post if")
        form = UserCreationForm(data=request.POST) 
        if form.is_valid():
            print("Passed form validation")
            user = form.save()
            login(request, user)
            print("Saved the form")
            #TODO show error message on screen 
            return redirect('/home')
        print("After form validation")
    else: 
        print("Not if method Creating new form")
        form = UserCreationForm() 
    return render(request,'signup.html',{'name':'LineUp Signup','form':form})
