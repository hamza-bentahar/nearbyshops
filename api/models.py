from django.db import models
from django.conf import settings
from django.db.models.expressions import RawSQL


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


def get_shops_by_distance(latitude=None, longitude=None):
    """
    Return objects sorted by distance to specified coordinates
    which distance is less than max_distance given in kilometers
    """
    distance_formula = "(((acos(sin((%s*pi()/180)) * sin((`latitude`*pi()/180)) + cos((%s*pi()/180)) " \
                       "* cos((`latitude`*pi()/180)) * cos(((%s- `longitude`) * pi()/180)))) " \
                       "* 180/pi()) * 60 * 1.1515 * 1.609344)"
    distance_raw_sql = RawSQL(distance_formula, (latitude, latitude, longitude))
    qs = Shop.objects.all()
    if latitude and longitude:
        qs = qs.annotate(distance=distance_raw_sql).order_by('distance')
    else:
        qs = qs.extra({'distance': -1}).order_by('id')
    return qs
