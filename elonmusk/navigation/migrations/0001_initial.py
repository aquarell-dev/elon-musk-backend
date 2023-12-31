# Generated by Django 4.2.3 on 2023-07-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(help_text='Название ссылки, которое будет отображаться в навигации сайта', max_length=64, unique=True, verbose_name='Название')),
                ('href', models.SlugField(help_text='Путь ссылки в браузере. Старайтесь делать коротким!', unique=True, verbose_name='Путь ссылки')),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
            },
        ),
    ]
