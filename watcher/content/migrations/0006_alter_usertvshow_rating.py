# Generated by Django 4.2.4 on 2023-09-21 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_movie_tvshow_usertvshow_usermovie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertvshow',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
