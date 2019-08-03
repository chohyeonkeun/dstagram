# Generated by Django 2.1 on 2019-08-03 16:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='like_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photo',
            name='saved',
            field=models.ManyToManyField(blank=True, null=True, related_name='saved_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
