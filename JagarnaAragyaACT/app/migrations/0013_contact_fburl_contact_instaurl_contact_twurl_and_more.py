# Generated by Django 4.2.2 on 2023-07-02 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_videos'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='fbUrl',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='instaUrl',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='twUrl',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='ubUrl',
            field=models.URLField(blank=True, null=True),
        ),
    ]
