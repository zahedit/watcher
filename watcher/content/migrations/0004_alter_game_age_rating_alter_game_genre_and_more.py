# Generated by Django 4.2.4 on 2023-09-16 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_alter_game_age_rating_alter_game_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='age_rating',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='game',
            name='platform',
            field=models.CharField(max_length=256),
        ),
    ]
