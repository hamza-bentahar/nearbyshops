from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ShopSerializer, ShopUserSerializer
from .models import Shop


class ShopList(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ShopDetail(RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class LikeShop(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, shop_pk):
        data = {'shop': shop_pk, 'like': 1, 'user': self.request.user.id}
        serializer = ShopUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
