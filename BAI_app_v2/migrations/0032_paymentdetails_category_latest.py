# Generated by Django 3.1.2 on 2020-12-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BAI_app_v2', '0031_usercategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetails',
            name='category_latest',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
