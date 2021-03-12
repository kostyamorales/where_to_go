from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название места', max_length=100, db_index=True)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    lat = models.FloatField('Долгота')
    lon = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField('Картинка', null=True)
    place = models.ForeignKey('Place', on_delete=models.CASCADE, null=True, related_name='imgs')
    order = models.PositiveIntegerField(default=0)

    class Meta():
        ordering = ('order',)

    def __str__(self):
        return f'{self.id} {self.place.title}'
