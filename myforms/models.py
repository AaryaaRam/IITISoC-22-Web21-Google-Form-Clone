from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class CreateForm(models.Model):
    name=models.CharField(max_length=40)
    dateOfForm=models.DateTimeField(default=timezone.now)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)