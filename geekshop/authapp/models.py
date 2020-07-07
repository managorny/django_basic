from django.db import models

from django.contrib.auth.models import User, AbstractUser


class ShopUser(AbstractUser):
    age = models.PositiveSmallIntegerField('Возраст', null=True)
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    id_for_friends = models.CharField('Код для пригашения друзей', max_length=8, blank=True)
