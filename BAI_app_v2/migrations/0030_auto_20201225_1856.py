# Generated by Django 3.1.2 on 2020-12-25 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BAI_app_v2', '0029_paymentdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='economy',
            name='category_latest',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='others',
            name='category_latest',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='project_info',
            name='category_latest',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='quality',
            name='category_latest',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='safetynwellfare',
            name='category_latest',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='speed',
            name='category_latest',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
