from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='' , verbose_name='عکس پروفایل')
    verify_code = models.CharField(max_length=6 , verbose_name='کد فعالسازی')
    token = models.CharField(max_length=100 , verbose_name='توکن' , blank=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'

    def generate_token(self):
        self.token = get_random_string(100)
        self.save()



    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

