from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='слаг')
    content = models.TextField(verbose_name='содержание')
    preview_image = models.ImageField(verbose_name='изображение')
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    is_published = models.BooleanField(verbose_name='опубликовано', default=True)
    views_counter = models.PositiveIntegerField(verbose_name='количество просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья блога'
        verbose_name_plural = 'статьи блога'
