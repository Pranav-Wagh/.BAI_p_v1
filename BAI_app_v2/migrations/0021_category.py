# Generated by Django 3.1.2 on 2020-11-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BAI_app_v2', '0020_auto_20201110_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users_name', models.CharField(blank=True, max_length=20)),
                ('app_form_cat', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], max_length=4)),
            ],
        ),
    ]