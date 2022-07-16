from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.shortcuts import render
from myforms.models import CreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

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

class FormOpenView(LoginRequiredMixin,DetailView):
    model=CreateForm

class CreateNewForm(LoginRequiredMixin,CreateView):
    model=CreateForm
    fields=['name']
    
    def form_valid(self,form):
        form.instance.owner=self.request.user
        return super().form_valid(form)
 
class UpdateForm(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=CreateForm
    fields=['name']
  
    def form_valid(self,form):
        form.instance.owner=self.request.user
        return super().form_valid(form)

    def test_func(self):
        gform=self.get_object()
        if self.request.user==gform.owner:
            return True
        return False

class DeleteForm(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=CreateForm
    success_url='/'

    def test_func(self):
        gform=self.get_object()
        if self.request.user==gform.owner:
            return True
        return False
