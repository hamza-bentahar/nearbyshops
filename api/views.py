from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ShopSerializer, ShopUserSerializer
from .models import Shop


class ShopList(ListAPIView):
    serializer_class = ShopSerializer

    def get_queryset(self):
        params = self.request.query_params
        if 'geo_lat' in params and 'geo_long' in params:
            query = "SELECT *, " \
                    "(((acos(sin((%s*pi()/180)) * sin((`latitude`*pi()/180)) + cos((%s*pi()/180)) * cos((`latitude`*pi()/180)) * cos(((%s- `longitude`) * pi()/180)))) * 180/pi()) * 60 * 1.1515 * 1.609344) as distance " \
                    "FROM `api_shop` ORDER BY distance"
            return Shop.objects.raw(query, [params['geo_lat'], params['geo_lat'], params['geo_long']])
        query = "SELECT *, -1 as distance FROM `api_shop`"
        return Shop.objects.raw(query)


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
