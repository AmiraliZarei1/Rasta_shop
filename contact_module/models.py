from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name = models.CharField(max_length=90 , verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    text = models.TextField(verbose_name='متن پیام')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'
