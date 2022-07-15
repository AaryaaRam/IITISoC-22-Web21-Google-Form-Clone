from django.contrib import admin

from myforms.models import CreateForm
from myforms.models import Profile

# Register your models here.
admin.site.register(CreateForm)
admin.site.register(Profile)