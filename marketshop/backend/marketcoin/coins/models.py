from django.db import models
from django.conf import settings
# Create your models here.

User=settings.AUTH_USER_MODEL

class Coin(models.Model):
    user= models.ForeignKey(User, default=1, null=True,on_delete=models.SET_NULL)
    name= models.CharField(max_length=50, blank=False, null=False)
    description= models.TextField(blank=True)
    price= models.DecimalField(max_digits=10, decimal_places=3, null=False)

