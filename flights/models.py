from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    image = models.ImageField(blank=True, null=True, default='', upload_to='countries/')