from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import ShopSerializer, ShopUserSerializer, RegisterSerializer
from .models import Shop, ShopUser, get_shops_by_distance
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json

index_view = never_cache(TemplateView.as_view(template_name='index.html'))


@ensure_csrf_cookie
def set_csrf_token(request):
    """
    This will be `/api/set-csrf-cookie/` on `urls.py`
    """
    return JsonResponse({"details": "CSRF cookie set"})


class Logout(APIView):
    def get(self, request):
        logout(request)
        return Response(status=200)


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


class Login(APIView):
    def post(self, request):
        """
        This will be `/api/login/` on `urls.py`
        """

        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return JsonResponse({
                "detail": "Please enter both username and password"
            }, status=400)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({
                "detail": "authenticated",
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
        user_latitude, user_longitude = None, None
        if 'geo_lat' in params and 'geo_long' in params:
            user_latitude, user_longitude = params['geo_lat'], params['geo_long']
        return get_shops_by_distance(user_latitude, user_longitude)


class LikedShopList(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        params = self.request.query_params
        user_latitude, user_longitude = None, None
        if 'geo_lat' in params and 'geo_long' in params:
            user_latitude, user_longitude = params['geo_lat'], params['geo_long']
        return get_shops_by_distance(user_latitude, user_longitude) \
            .filter(shopuser__user=self.request.user.id)


class ShopDetail(RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get_queryset(self):
        params = self.request.query_params
        user_latitude, user_longitude = None, None
        if 'geo_lat' in params and 'geo_long' in params:
            user_latitude, user_longitude = params['geo_lat'], params['geo_long']
        return get_shops_by_distance(user_latitude, user_longitude)


class UnlikeShop(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, shop_pk):
        ShopUser.objects.filter(**{'shop': shop_pk, 'user': self.request.user.id}).delete()
        return Response({
            "details": "deleted"
        })


class LikeShop(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, shop_pk):
        data = {'shop': shop_pk, 'like': 1, 'user': self.request.user.id}
        serializer = ShopUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
