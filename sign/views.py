from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account Created {username}')
            return redirect('signin')
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{'form':form})

def signin(request):
    return render(request,'signin.html')

def signout(request):
    return 0