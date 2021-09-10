from django.urls import path
from api.views import ShopList, ShopDetail, LikeShop

urlpatterns = [
    path('shops/', ShopList.as_view(), name='shop-list'),
    path('shops/<str:pk>/', ShopDetail.as_view(), name='shop-detail'),
    path('shops/<str:shop_pk>/like/', LikeShop.as_view(), name='shop-like'),
]
