# Generated by Django 4.1 on 2022-08-10 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainuser', '0003_rename_end_date_experience_end_date_e_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='profile',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='profile',
            new_name='user',
        ),
    ]
