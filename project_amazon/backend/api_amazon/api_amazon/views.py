from django.shortcuts import render
from rest_framework import generics

from api_amazon import models
from api_amazon.serializers import ItemSerializer, PhotoSerializer

def test_img(request, pk=None):
    item_pic= models.Photo.objects.get(pk=pk)

    return render(request, 'test.html', context={'img':item_pic})


class ItemListCreateViewAPI(generics.ListCreateAPIView):
    queryset= models.Item.objects.all()
    serializer_class=ItemSerializer


class ItemDetailViewAPI(generics.RetrieveAPIView):
    queryset= models.Item.objects.all()
    serializer_class= ItemSerializer


class ItemUpdateViewAPI(generics.UpdateAPIView):
    queryset= models.Item.objects.all()
    serializer_class=ItemSerializer
    lookup_field= 'pk'


class ItemDeleteViewAPI(generics.DestroyAPIView):
    queryset=models.Item.objects.all()
    serializer_class= ItemSerializer
    lookup_field= 'pk'





class PhotoListCreateViewAPI(generics.ListCreateAPIView):
    queryset= models.Photo.objects.all()
    serializer_class= PhotoSerializer

