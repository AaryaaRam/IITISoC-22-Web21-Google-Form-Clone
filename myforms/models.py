from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class CreateForm(models.Model):
    name=models.CharField(max_length=40)
    dateOfForm=models.DateTimeField(default=timezone.now)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=40,default="")

    def __str__(self):
        return f'{self.user.username}'