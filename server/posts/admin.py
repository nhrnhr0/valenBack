from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'is_published')
    readonly_fields = ('created_at', 'updated_at')

    prepopulated_fields = {"slug": ("title",)}
    pass
admin.site.register(Post, PostAdmin)