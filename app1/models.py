from django.db import models
import email

# Create your models here.
class Raj(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    place = models.CharField(max_length=100)
    phonenumber = models.IntegerField()
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.name