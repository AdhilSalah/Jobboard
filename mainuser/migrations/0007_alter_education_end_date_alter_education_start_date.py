# Generated by Django 4.1 on 2022-08-10 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainuser', '0006_rename_profile_education_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]