from django.urls import path
from api.views import ShopList, ShopDetail, LikeShop, set_csrf_token, login_view

urlpatterns = [
    path('shops/', ShopList.as_view(), name='shop-list'),
    path('shops/<str:pk>/', ShopDetail.as_view(), name='shop-detail'),
    path('shops/<str:shop_pk>/like/', LikeShop.as_view(), name='shop-like'),
    path('login/', login_view, name='Login'),
    path('set-csrf-cookie/', set_csrf_token, name='set_csrf_token'),
]
