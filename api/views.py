from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ShopSerializer, ShopUserSerializer
from .models import Shop


class ShopList(ListAPIView):
    geo_long = -6.8150925
    geo_lat = 33.916744
    query = f"SELECT *, " \
            f"(((acos(sin(({geo_lat}*pi()/180)) * sin((`latitude`*pi()/180)) + cos(({geo_lat}*pi()/180)) * cos((`latitude`*pi()/180)) * cos((({geo_long}- `longitude`) * pi()/180)))) * 180/pi()) * 60 * 1.1515 * 1.609344) as distance " \
            f"FROM `api_shop` ORDER BY distance"
    queryset = Shop.objects.raw(query)
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
