from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from coins.models import Coin

def validate_title(value):
    qs=Coin.objects.filter(name__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f'{value} already exists')
    return value