from django.contrib import admin

# Register your models here.
from article_module.models import ArticleModel


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title' , 'author']
    exclude = ['author']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
            return super(ArticleAdmin, self).save_model(request, obj, form, change)
        else:
            pass


admin.site.register(ArticleModel , ArticleAdmin)