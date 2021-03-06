from django.db import models


# Create your models here.
class Place(models.Model):
    title = models.CharField('Название места', max_length=100)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = models.TextField('Полное описание', blank=True)
    lat = models.FloatField('Долгота')
    lon = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField('Фото', null=True)
    place = models.ForeignKey('Place', verbose_name='Название места', on_delete=models.CASCADE, null=True,
                              related_name='imgs')

    def __str__(self):
        return f'{self.id} {self.place.title}'
