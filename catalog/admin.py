from django.contrib import admin
from catalog.models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price_buy")
    list_filter = ("category",)
    search_fields = ("name", "description")