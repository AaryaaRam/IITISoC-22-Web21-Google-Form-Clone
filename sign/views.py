from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth import login,logout

# Create your views here.

def signup(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account Created {username}')
            return redirect('signin')
    else:
        form=RegistrationForm()
    return render(request,'signup.html',{'form':form})

def signin(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request,f"logged in succefully. Welcome {username}")
            user=form.get_user()
            login(request,user)
            return redirect('form-home')
    else:
        form=AuthenticationForm()
    return render(request,'signin.html',{'form':form})

def signout(request):
    if request.method=='POST':
        logout(request)
        messages.success(request,f"logged out successfully ")
    return redirect('signin')