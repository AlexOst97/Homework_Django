from django.contrib import admin
from blog.models import Blogs


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "views")
    list_filter = ("is_active", "views")
    search_fields = ("title", "contents")