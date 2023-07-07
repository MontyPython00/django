from django.db import models

# Create your models here.

class Pricing(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name}, Price:{self.price}"

class Account(models.Model):
    login = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

