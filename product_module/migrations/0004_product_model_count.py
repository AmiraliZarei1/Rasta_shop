# Generated by Django 5.1 on 2024-09-04 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_alter_product_model_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_model',
            name='count',
            field=models.IntegerField(default=1, verbose_name='تعداد'),
            preserve_default=False,
        ),
    ]
