from django.db import models


class Benefit(models.Model):
    top = models.CharField('Верхний текст', max_length=32, help_text='Текст, который будет отображен в верхней части блока преимуществ')
    middle = models.CharField('Средний текст', max_length=32, help_text='Текст, который будет отображен в середине блока преимуществ')
    bottom = models.CharField('Нижний текст', max_length=32, help_text='Текст, который будет отображен в нижней части блока преимуществ')

    def __str__(self):
        return f'Преимущество {self.id}'

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
