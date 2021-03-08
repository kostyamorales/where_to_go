from django.shortcuts import render
from places.models import Place
from django.urls import reverse


def index(request):
    places = Place.objects.all()
    features = {
        'type': 'FeatureCollection',
        'features': [],
    }
    for place in places:
        features['features'].append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [
                    place.lon,
                    place.lat
                ]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place', args=[place.id])
            }
        })

    places_geojson = {
        'places': features
    }
    return render(request, 'index.html', context=places_geojson)
