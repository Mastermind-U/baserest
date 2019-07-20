from django.contrib.auth.models import User
from django.db import models
# from djoser.urls.base import User


class Room(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')
    visitors = models.ManyToManyField(User, related_name='visitors')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Chat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Сообщение', max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
