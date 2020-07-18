from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .task import post_created


class Post(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название публикации')
    text = models.TextField(max_length=2000, verbose_name='Текст публикации')
    image = models.ImageField(verbose_name='Прикрепленное изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


@receiver(post_save, sender=Post, dispatch_uid='post_new')
def post_signal(sender, instance, **kwargs):
    return post_created.delay(instance.id)
