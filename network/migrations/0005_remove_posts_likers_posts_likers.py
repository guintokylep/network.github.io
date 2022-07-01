# Generated by Django 4.0.4 on 2022-06-22 09:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_remove_profile_followers_profile_followers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='likers',
        ),
        migrations.AddField(
            model_name='posts',
            name='likers',
            field=models.ManyToManyField(blank=True, null=True, related_name='likers', to=settings.AUTH_USER_MODEL),
        ),
    ]