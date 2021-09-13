from django.urls import path
from api.views import ShopList, ShopDetail, LikeShop, set_csrf_token, \
    login_view, IsUserAuthenticated, Logout, RegisterView, LikedShopList, UnlikeShop

urlpatterns = [
    path('shops/', ShopList.as_view(), name='shop-list'),
    path('shops/<str:pk>/', ShopDetail.as_view(), name='shop-detail'),
    path('shops/<str:shop_pk>/like/', LikeShop.as_view(), name='shop-like'),
    path('shops/<str:shop_pk>/unlike/', UnlikeShop.as_view(), name='shop-unlike'),
    path('likedshops/', LikedShopList.as_view(), name='liked-shops'),
    path('login/', login_view, name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('set-csrf-cookie/', set_csrf_token, name='set_csrf_token'),
    path('isauthenticated/', IsUserAuthenticated.as_view(), name='is_authenticated'),
]
