from rest_framework import serializers
from api_amazon import models


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Item
        fields=[
            'id',
            'product',
            'item_owner',
            'price',
            'description',
            'item_picture',        
        ]

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Photo
        fields=[
            'name',
            'item_img',
            'user',
        ]