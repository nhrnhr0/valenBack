from django.contrib import admin
from .models import GalleryImage
from django.utils.safestring import mark_safe

# Register your models here.
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('created_at','id', 'rendered_image','alt', 'updated_at', 'is_published', 'address',)
    readonly_fields = ('created_at', 'updated_at','location',)

    prepopulated_fields = {"slug": ("alt",)}
    
    def rendered_image(self, obj):
        return mark_safe('<img src="{url}" width="50px" height="50px" />'.format(
            url = obj.image.url))

    pass
admin.site.register(GalleryImage, GalleryImageAdmin)