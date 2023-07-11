from django.db import models


class NavigationLink(models.Model):
    link = models.CharField(
        'Название',
        max_length=64,
        help_text='Название ссылки, которое будет отображаться в навигации сайта',
        unique=True
    )
    href = models.SlugField(
        'Путь ссылки',
        unique=True,
        null=True,
        blank=True,
        help_text='Путь ссылки в браузере. Старайтесь делать коротким!',
    )
    order = models.PositiveSmallIntegerField(
        'Приоритет Ссылки',
        unique=True,
        help_text='Позиция Ссылки В Навигационной Панели'
    )

    def __str__(self):
        return f'Ссылка {self.link}'

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
