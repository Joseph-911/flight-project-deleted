from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    image = models.ImageField(blank=True, null=True, default='', upload_to='countries/')

    def __str__(self):
        return f'{self.name}'
    

class Flight(models.Model):
    pass


class Ticket(models.Model):
    pass