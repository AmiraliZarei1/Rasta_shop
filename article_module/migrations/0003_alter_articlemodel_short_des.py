# Generated by Django 5.1 on 2024-09-03 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0002_articlemodel_author_articlemodel_short_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='short_des',
            field=models.CharField(max_length=500, verbose_name='فعال/غیرفعال'),
        ),
    ]
