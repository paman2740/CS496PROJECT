# Generated by Django 4.0.2 on 2022-04-23 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law_enforcement', '0010_alter_photo_image_alter_user_login_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 23, 16, 57, 17, 849469)),
        ),
        migrations.AlterField(
            model_name='user',
            name='logout_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 23, 16, 57, 17, 849469)),
        ),
    ]
