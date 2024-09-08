from django.db import models
from product_module.models import Product_Model
from user_module.models import User


# Create your models here.



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , verbose_name='کاربر')
    is_paid = models.BooleanField(default=False , verbose_name='پرداخت شده/نشده')
    paid_date = models.DateTimeField(null=True , verbose_name='تاریخ پرداخت')
    ostan = models.CharField(max_length=100 , null=True , verbose_name='استان')
    city = models.CharField(max_length=100 , null=True , verbose_name='شهر')
    address = models.CharField(max_length=100 , null=True , verbose_name='ادرس')

    def __str__(self):
        return self.user.username

    def total_price(self):
        final = 0
        for detail in self.orderdetail_set.all():
            final += (detail.count * detail.product.price)
        return final


    def fee(self):
        return round(self.total_price() * 0.1)

    def final_price(self):
        return round(self.fee() + self.total_price())




    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'



class OrderDetail(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE , verbose_name='سبد خرید')
    product = models.ForeignKey(Product_Model , on_delete=models.CASCADE , verbose_name='محصول')
    final_price = models.IntegerField(verbose_name='قیمت نهایی')
    count = models.IntegerField(verbose_name='تعداد')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'جزییات سبد های خرید'



