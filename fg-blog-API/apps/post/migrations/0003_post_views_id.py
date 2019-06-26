# Generated by Django 2.2.2 on 2019-06-26 21:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_auto_20190620_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views_id',
            field=models.ManyToManyField(related_name='user_views', to=settings.AUTH_USER_MODEL),
        ),
    ]
