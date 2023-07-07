from coins.serializers import CoinSerializer
from coins.models import Coin
from coins.permissions import CoinEditorPermissions
from rest_framework import generics, authentication, permissions

# Create your views here.

class CoinListViewAPI(generics.ListAPIView):
    queryset=Coin.objects.all()
    serializer_class=CoinSerializer


class CoinDetailView(generics.RetrieveAPIView):
    queryset=Coin.objects.all()
    serializer_class=CoinSerializer
    lookup_field='name'


class CoinListCreateViewAPI(generics.ListCreateAPIView):
    queryset=Coin.objects.all()
    serializer_class=CoinSerializer
    authentication_classes=[authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser, CoinEditorPermissions]

    def perform_create(self, serializer):
        name=serializer.validated_data.get('name')
        description=serializer.validated_data.get('description') or None
        if description is None:
            description=name
        return serializer.save(user=self.request.user,description=description)
    
    def get_queryset(self, *args, **kwargs):
        qs= super().get_queryset(*args, **kwargs)
        request= self.request
        return qs.filter(user=request.user)


class CoinDetailViewAPI(generics.RetrieveAPIView):
    queryset=Coin.objects.all()
    serializer_class=CoinSerializer
    lookup_field='pk'
    authentication_classes=[authentication.SessionAuthentication,authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser, CoinEditorPermissions]


class CoinDeleteViewAPI(generics.DestroyAPIView):
    queryset=Coin.objects.all()
    serializer_class=CoinSerializer
    lookup_field='pk'
    authentication_classes=[authentication.SessionAuthentication,authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser, CoinEditorPermissions]


class CoinUpdateViewAPI(generics.UpdateAPIView):
    queryset=Coin.objects.all()
    serializer_class=CoinSerializer
    lookup_field='pk'
    authentication_classes=[authentication.SessionAuthentication,authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser, CoinEditorPermissions]



    




