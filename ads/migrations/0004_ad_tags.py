# Generated by Django 4.0.7 on 2023-03-14 17:49

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('ads', '0003_fav_ad_favorites_fav_ad_fav_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
