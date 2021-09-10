from django.db import models
from django.conf import settings


# Create your models here.
class Shop(models.Model):
    picture = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    latitude = models.DecimalField(max_digits=7, decimal_places=5)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='ShopUser')


class ShopUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    like = models.BooleanField()

    class Meta:
        unique_together = ('shop', 'user',)
