from django.urls import path

from article_module.views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('' , ArticleListView.as_view() , name='article_list') ,
    path('single-article/<id>' , ArticleDetailView.as_view() , name='article_detail')
]