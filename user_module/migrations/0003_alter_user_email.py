# Generated by Django 5.0.6 on 2024-07-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0002_rename_avatar_user_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل'),
        ),
    ]
