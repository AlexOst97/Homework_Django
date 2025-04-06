from django.db import models


class Blogs(models.Model):
    """Класс, для блоговой записи"""

    title = models.CharField(max_length=150, verbose_name='Заголовок', help_text='Введите заголовок')
    contents = models.TextField(blank=True, null=True, verbose_name='Содержимое', help_text='Введите содержимое')
    image = models.ImageField(upload_to='blog/image', blank=True, null=True, verbose_name='Изображение', help_text='Загрузите изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Признак публикации', help_text='Введите признак публикации')
    views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров', help_text='Введите количество просмотров')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['title', 'created_at', 'is_active', 'views']

    def __str__(self):
        return f'{self.title}'