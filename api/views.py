from rest_framework.decorators import api_view
from rest_framework.response import Response


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
