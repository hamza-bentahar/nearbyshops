from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ShopSerializer
from .models import Shop


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'preferred': '/preferred',
        'preferredData': '/preferredData',
        'nearby': '/nearby',
        'like': '/like',
        'dislike': '/dislike'
    }
    return Response(api_urls)


@api_view(['GET'])
def shop_list(request):
    shops = Shop.objects.all()
    serializer = ShopSerializer(shops, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def shop_detail(request, shop_id):
    shops = Shop.objects.get(id=shop_id)
    serializer = ShopSerializer(shops, many=False)
    return Response(serializer.data)
