# Generated by Django 4.2.9 on 2024-07-13 05:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_inquiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
