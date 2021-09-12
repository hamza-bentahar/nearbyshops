from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ShopSerializer, ShopUserSerializer
from .models import Shop
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login
import json

index_view = never_cache(TemplateView.as_view(template_name='index.html'))


@ensure_csrf_cookie
def set_csrf_token(request):
    """
    This will be `/api/set-csrf-cookie/` on `urls.py`
    """
    return JsonResponse({"details": "CSRF cookie set"})


class IsUserAuthenticated(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return JsonResponse({
                "detail": "authenticated",
                "user": str(request.user)
            })
        else:
            return JsonResponse({
                "detail": "unauthenticated"
            })


@require_POST
def login_view(request):
    """
    This will be `/api/login/` on `urls.py`
    """
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    if username is None or password is None:
        return JsonResponse({
            "errors": {
                "__all__": "Please enter both username and password"
            }
        }, status=400)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({
            "detail": "Success",
            "user": str(user)
        })
    return JsonResponse(
        {"detail": "Invalid credentials"},
        status=400,
    )


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
