from django.db import models

class Category(models.Model):
    '''Класс категорий'''

    name = models.CharField(max_length=150, verbose_name='Наименование', help_text='Введите наименование категории')
    description = models.TextField(blank=True, null=True, verbose_name='Описание', help_text='Введите описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    '''Класс продуктов'''

    name = models.CharField(max_length=150, verbose_name='Наименование', help_text='Введите наименование продукта')
    description = models.TextField(blank=True, null=True, verbose_name='Описание', help_text='Введите описание продукта')
    image = models.ImageField(upload_to='catalog/image',blank=True, null=True, verbose_name='Изображение', help_text='Загрузите изображение продукта')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', help_text='Введите категорию продукта')
    price_buy = models.IntegerField(verbose_name='Цена за покупку', help_text='Введите цену за покупку продукта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category', 'price_buy', 'created_at', 'updated_at']

    def __str__(self):
        return f'{self.name}'
