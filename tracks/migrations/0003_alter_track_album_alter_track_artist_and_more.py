# Generated by Django 5.1.4 on 2024-12-24 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0002_alter_track_album_alter_track_artist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='track',
            name='artist',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='track',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]