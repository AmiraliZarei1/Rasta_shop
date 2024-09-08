from django.contrib import admin
from .models import *
# Register your models here.

class ProductModelAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        'slug' : ['title']
    }


admin.site.register(Product_Model , ProductModelAdmin)
admin.site.register(ProductComment_Model)