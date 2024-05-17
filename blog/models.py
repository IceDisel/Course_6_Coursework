from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='previews/', verbose_name='Изображение', **NULLABLE)
    published_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['title']

    def __str__(self):
        return self.title
