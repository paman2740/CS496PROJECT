# Generated by Django 4.0.2 on 2022-04-13 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law_enforcement', '0008_alter_user_login_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='logout_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 12, 41, 16, 195592)),
        ),
        migrations.AlterField(
            model_name='user',
            name='login_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 13, 12, 41, 16, 195592)),
        ),
    ]
