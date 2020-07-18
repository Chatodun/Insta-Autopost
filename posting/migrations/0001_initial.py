# Generated by Django 3.0.8 on 2020-07-18 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название публикации')),
                ('text', models.TextField(max_length=2000, verbose_name='Текст публикации')),
                ('image', models.ImageField(upload_to='', verbose_name='Прикрепленное изображение')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
