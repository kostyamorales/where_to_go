from places.models import Place, Image
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def show_place_page(request, id):
    place = get_object_or_404(Place, id=id)
    imgs = [img.img.url for img in place.imgs.all()]
    place_json = {
        'title': place.title,
        'imgs': imgs,
        'description_short': place.short_description,
        'description_long': place.long_description,
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
