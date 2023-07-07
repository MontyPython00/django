from rest_framework import serializers
from coins.models import Coin
from coins.validators import validate_title


class CoinSerializer(serializers.ModelSerializer):
    name= serializers.CharField(validators=[validate_title])
    class Meta:
        model= Coin
        fields=['id', 'name', 'description', 'price']