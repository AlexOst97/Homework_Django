from .models import Product, Category

class CategoryService:

    @staticmethod
    def get_products_by_category(category_id):
        category = Category.objects.get(id=category_id)
        product = Product.objects.filter(category=category)
        return f"{product.name}"