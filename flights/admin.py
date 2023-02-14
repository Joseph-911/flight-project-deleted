from django.contrib import admin
from .models import Country

# Register your models here.
myModels = [Country]
admin.site.register(myModels)