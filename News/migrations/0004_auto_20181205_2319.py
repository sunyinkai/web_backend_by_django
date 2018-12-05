# Generated by Django 2.1.3 on 2018-12-05 15:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_comment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date',
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 5, 15, 19, 51, 246742, tzinfo=utc)),
        ),
    ]
