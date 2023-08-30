# Generated by Django 4.2.4 on 2023-08-30 08:39

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_nickname_alter_user_email_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=user.models.get_avatar_path),
        ),
    ]
