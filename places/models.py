from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название места', max_length=100, db_index=True)
    short_description = models.TextField('Краткое описание', blank=True)
    long_description = HTMLField('Полное описание', blank=True)
    lat = models.FloatField('Долгота')
    lon = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField('Картинка')
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='imgs')
    order = models.PositiveIntegerField(default=0, blank=True)

    class Meta():
        ordering = ('order',)

    def __str__(self):
        return f'{self.id} {self.place.title}'
