# Generated by Django 5.0.6 on 2024-08-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logos', verbose_name='لوگو')),
                ('phone_number', models.CharField(max_length=20, verbose_name='شماره نلفن')),
                ('email', models.CharField(max_length=50, verbose_name='ایمیل')),
                ('about', models.TextField(verbose_name='متن درباره ما')),
            ],
            options={
                'verbose_name': 'تنظیم',
                'verbose_name_plural': 'تنظیمات',
            },
        ),
    ]
