import os
from django.core.management.base import BaseCommand
from places.models import Place
import json
from io import BytesIO
import requests


def loads_imgs(place, urls):
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
        for file_name in os.listdir('static/places'):
            if file_name.endswith('.json'):
                with open(f'static/places/{file_name}') as file:
                    place_feature = json.loads(file.read())
                    imgs_urls = place_feature['imgs']
                    place, created = Place.objects.get_or_create(
                        title=place_feature['title'],
                        description_short=place_feature['description_short'],
                        description_long=place_feature['description_long'],
                        lat=place_feature['coordinates']['lat'],
                        lon=place_feature['coordinates']['lng']
                    )
                    place.save()
                    loads_imgs(place, imgs_urls)
