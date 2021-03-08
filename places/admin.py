from django.contrib import admin
from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ('img', 'id', 'place')
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(Image)
class PlaceAdmin(admin.ModelAdmin):
    pass
