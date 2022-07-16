from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path
from myforms import views
from myforms.views import FormOpenView,CreateNewForm,UpdateForm,DeleteForm

urlpatterns = [
    path('',views.home,name="form-home"),
    path('profile/',views.about,name="form-profile"),
    path('form/<int:pk>/',FormOpenView.as_view(),name="form-view"),
    path('form/new/',CreateNewForm.as_view(),name="form-create"),
    path('form/<int:pk>/update/',UpdateForm.as_view(),name="form-update"),
    path('form/<int:pk>/delete/',DeleteForm.as_view(),name="form-delete")
]