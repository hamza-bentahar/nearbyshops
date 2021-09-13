from rest_framework import serializers
from .models import Shop, ShopUser
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class ShopSerializer(serializers.ModelSerializer):
    distance = serializers.DecimalField(10, 2)
    liked = serializers.SerializerMethodField(method_name='is_liked')

    class Meta:
        model = Shop
        fields = ['id', 'picture', 'name', 'email', 'city', 'longitude', 'latitude', 'distance', 'liked']

    def is_liked(self, shop):
        return shop.users.filter(id=self.context['request'].user.id).exists()


class ShopUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = ['like', 'user', 'shop']


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirmation = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirmation', 'email', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
