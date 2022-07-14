from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="form-home"),
    path('profile/',views.about,name="form-profile")
]