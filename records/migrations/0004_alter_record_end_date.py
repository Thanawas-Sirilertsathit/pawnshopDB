# Generated by Django 5.1 on 2024-11-10 02:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_remove_pawnshop_user_alter_record_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 11, 10, 2, 54, 31, 567972, tzinfo=datetime.timezone.utc)),
        ),
    ]
