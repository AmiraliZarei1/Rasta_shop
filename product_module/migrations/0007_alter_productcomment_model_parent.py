# Generated by Django 5.1 on 2024-09-06 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0006_alter_productcomment_model_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomment_model',
            name='parent',
            field=models.ManyToManyField(blank=True, to='product_module.productcomment_model', verbose_name='والد'),
        ),
    ]
