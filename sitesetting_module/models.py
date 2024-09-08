from django.db import models

# Create your models here.


class SiteSettingModel(models.Model):
    logo = models.ImageField(upload_to='images/logos' , verbose_name='لوگو')
    phone_number = models.CharField(max_length=20 , verbose_name='شماره نلفن')
    email = models.CharField(max_length=50 , verbose_name='ایمیل')
    about = models.TextField(verbose_name='متن درباره ما')
    location = models.CharField(max_length=200 , verbose_name='مکان')
    is_active = models.BooleanField(default=True , verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.phone_number


    class Meta:
        verbose_name = 'تنظیم'
        verbose_name_plural = 'تنظیمات'



class SliderModel(models.Model):
    image = models.ImageField(upload_to='images/sliders' , verbose_name='تصویر اسلاید')
    title = models.CharField(max_length=20 , verbose_name='عنوان')
    link = models.URLField(max_length=200 , verbose_name='لینک')
    is_active = models.BooleanField(default=True , verbose_name='فعال/غیرفعال')
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'