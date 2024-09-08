from django.db import models

# Create your models here.
from user_module.models import User





class ArticleModel(models.Model):
    title = models.CharField(max_length=200 , verbose_name='عنوان')
    image = models.ImageField(upload_to='images/Article-images' , verbose_name='تصویر')
    create_date = models.DateTimeField(auto_now_add=True , verbose_name='تاریخ ثبت')
    text = models.TextField(verbose_name='توضیحات')
    short_des = models.CharField(max_length=600 ,  verbose_name='توضیحات کوتاه')
    author = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name='نویسنده' , null=True)
    slug = models.SlugField(unique=True , db_index=True , allow_unicode=True , verbose_name='ادرس در مرورگر')
    is_active = models.BooleanField(default=True , verbose_name='فعال/غیرفعال')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'