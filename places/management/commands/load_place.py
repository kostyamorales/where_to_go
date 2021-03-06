import os
from django.core.management.base import BaseCommand
from places.models import Place
import json
from io import BytesIO
import requests


def upload_imgs(place, urls):
    for num, url in enumerate(urls, 0):
        r = requests.get(url)
        r.raise_for_status()
        img = BytesIO(r.content)
        img_name = os.path.basename(url)
        image, created = place.imgs.get_or_create(place=place.title, order=num)
        image.img.save(img_name, img, save=True)


class Command(BaseCommand):
    help = 'loads new places'

    def handle(self, *args, **options):
        for file_name in os.listdir('places_json'):
            if not file_name.endswith('.json'):
                continue
            with open(f'places_json/{file_name}') as file:
                place_feature = json.loads(file.read())
            imgs_urls = place_feature['imgs']
            place, created = Place.objects.update_or_create(title=place_feature['title'], defaults={
                'short_description': place_feature['description_short'],
                'long_description': place_feature['description_long'],
                'lat': place_feature['coordinates']['lat'],
                'lon': place_feature['coordinates']['lng']
            })
            upload_imgs(place, imgs_urls)