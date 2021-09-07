from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('shops/', views.shop_list, name='shop-list'),
    path('shops/<str:shop_id>/', views.shop_detail, name='shop-detail'),
]
