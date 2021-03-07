from places.models import Place, Image
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def show_place_page(request, id):
    place = get_object_or_404(Place, id=id)
    imgs = [img.img.url for img in Image.objects.filter(place=place)]
    place_json = {
        'title': place.title,
        'imgs': imgs,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lon
        }
    }
    response = JsonResponse(place_json, safe=False, json_dumps_params={
        'ensure_ascii': False,
        'indent': 4
    })
    return response
