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
        width = obj.img.width
        height = obj.img.height
        max_height = 200

        scale = height / max_height
        if scale > 1:
            height = max_height
            width = int(width / scale)

        return format_html(f'<img src="{obj.img.url}" width="{width}" height={height} />')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
