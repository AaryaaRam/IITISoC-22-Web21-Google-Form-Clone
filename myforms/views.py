from django.views.generic import ListView,DetailView,CreateView,DeleteView
from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.shortcuts import render
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

class FormList(ListView):
    model=CreateForm
    template_name='form.html'
    context_object_name='gform'
    order_by=['date-posted']

class FormOpenView(DetailView):
    model=CreateForm

class CreateNewForm(CreateView):
    model=CreateForm
    fields=['name']
    
    def form_valid(self,form):
        form.instance.owner=self.request.user
        return super().form_valid(form)
