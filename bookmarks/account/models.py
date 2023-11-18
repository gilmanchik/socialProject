from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                )

    day_of_birth = models.DateField(blank=True, null=True, verbose_name='День рождения')

    photo = models.ImageField(upload_to='user/%Y/%m/%d', verbose_name='Фото', blank=True)

    def __str__(self):
        return f'Profile for {self.user.username}'