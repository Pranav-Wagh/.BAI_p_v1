# Generated by Django 3.1.2 on 2020-10-29 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BAI_app_v2', '0004_auto_20201030_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speed',
            name='mechanization',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
