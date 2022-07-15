from msilib.schema import ListView
from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.shortcuts import render
from myforms.models import CreateForm

from myforms.models import CreateForm

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='accounts/signin')
def home(request):
    context={
        'gforms':CreateForm.objects.all()
    }
    return render(request,'home.html',context)

@login_required(login_url='signin')
def about(request):
    return render(request,'profile.html')