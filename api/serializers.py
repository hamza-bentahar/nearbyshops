from rest_framework import serializers
from .models import Shop, ShopUser


class ShopSerializer(serializers.ModelSerializer):
    distance = serializers.DecimalField(10,2)

    class Meta:
        model = Shop
        fields = ['id', 'picture', 'name', 'email', 'city', 'longitude', 'latitude', 'distance']


class ShopUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = ['like', 'user', 'shop']
