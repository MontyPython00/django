from django.db import models

# Create your models here.



class CoinRequest(models.Model):
    name=models.CharField(max_length=30, blank=False)
    description=models.TextField(max_length=1200, blank=False)
    price=models.IntegerField(null=False)
    
    choice_status=(
        ('p', 'pending'),
        ('a', 'approved'),
        ('d', 'denied'),
    )

    status=models.CharField(max_length=1,choices=choice_status, default='p')

