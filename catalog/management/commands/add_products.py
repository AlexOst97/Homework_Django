from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Одежда', description='Раздел продажи одежды')

        products = [
            {'name': 'Красная футболка', 'description': 'Хлопковая футболка',
             'image': '','category': category, 'price_buy': 1500},
            {'name': 'Синие джинсы', 'description': 'Классические синие джинсы', 'image': '',
             'category': category, 'price_buy': 2200}
        ]
        for product_in_data in products:
            product, created = Product.objects.get_or_create(**product_in_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added book: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Book already exists: {product.name}'))