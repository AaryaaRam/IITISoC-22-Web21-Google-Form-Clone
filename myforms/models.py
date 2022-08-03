from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class CreateForm(models.Model):
    name=models.CharField(max_length=40)
    dateOfForm=models.DateTimeField(default=timezone.now)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse("form-view", kwargs={"pk": self.pk})


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=user.name
    
    def __str__(self):
        return f'{self.user.username}'

