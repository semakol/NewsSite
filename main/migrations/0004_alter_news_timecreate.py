# Generated by Django 3.2.5 on 2021-07-27 08:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_news_timecreate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='TimeCreate',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 27, 13, 13, 57, 150699), verbose_name='Время создания'),
        ),
    ]
