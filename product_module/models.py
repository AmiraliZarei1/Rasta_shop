from django.contrib.admin.utils import model_format_dict
from django.db import models

from user_module.models import User


# Create your models here.


class Product_Model(models.Model):
    title = models.CharField(max_length=185 , verbose_name='اسم محصول')
    price = models.IntegerField(verbose_name="قیمت")
    count = models.IntegerField(verbose_name="تعداد")
    image = models.ImageField(upload_to='images/P-images' , verbose_name='تصویر')
    ShortDes = models.CharField(max_length=285 , verbose_name='توضیحات(کوتاه)' , null=True)
    LongDes = models.TextField(verbose_name="توضیحات" , null=True)
    IsDelete = models.BooleanField(default=False , verbose_name="پاک شده / پاک نشده")
    IsActive = models.BooleanField(default=True , verbose_name="فعال / غیرفعال")
    slug = models.SlugField(default='' , null=False  , unique=True , allow_unicode = True , verbose_name='عنوان در مرورگر' )


    def __str__(self):
        return self.title


    class Meta :
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"



class ProductComment_Model(models.Model):
    product = models.ForeignKey(Product_Model , on_delete=models.CASCADE , verbose_name='محصول')
    user = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name='کاربر')
    text = models.TextField(verbose_name='متن نظر')
    create_date = models.DateTimeField(auto_now_add=True , verbose_name='زمان ارسال')
    parent = models.ForeignKey('ProductComment_Model' , on_delete=models.CASCADE , verbose_name='والد' , blank=True , null=True)

    def __str__(self):
        if self.user.first_name:
            return f'{self.user.first_name} , {self.user.last_name}'
        else:
            return self.user.username

    class Meta :
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"