from django.contrib import admin
from places.models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ('img', 'place', 'get_img_preview')
    extra = 1
    readonly_fields = ('get_img_preview',)

    def get_img_preview(self, obj):
        if obj.img:
            return format_html('<img src="{}" height="{}">', obj.img.url, 200)
        return 'Картинка ещё не загружена'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    search_fields = ('title',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place',)
