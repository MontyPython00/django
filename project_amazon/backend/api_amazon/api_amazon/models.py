from django.db import models
from django.contrib.auth.models import User
import os

class Photo(models.Model):
    name= models.CharField(max_length=100, null=False, blank=False)
    item_img= models.ImageField()
    user= models.CharField(max_length=70, null=False, blank=False)

    def __str__(self):
        return self.name

class Item(models.Model):
    product= models.CharField(max_length=70, null=False, blank=False)
    item_owner= models.CharField(max_length=30, null=False, blank=False)
    price= models.DecimalField(decimal_places=2, max_digits=7)
    description= models.CharField(max_length=1024)
    item_picture= models.ForeignKey('Photo', on_delete=models.SET_NULL, null=True)


