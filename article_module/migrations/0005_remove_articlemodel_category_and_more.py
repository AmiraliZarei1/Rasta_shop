# Generated by Django 5.1 on 2024-09-07 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0004_alter_articlemodel_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlemodel',
            name='category',
        ),
        migrations.DeleteModel(
            name='ArticleCategoryModel',
        ),
    ]
