from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from myforms.models import CreateForm

# Create your views here.

def home(request):
    context={
        'gforms':CreateForm.objects.all()
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'profile.html')