# Generated by Django 5.1 on 2024-09-03 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0006_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default=2, max_length=254, verbose_name='email address'),
            preserve_default=False,
        ),
    ]
