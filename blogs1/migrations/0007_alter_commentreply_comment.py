# Generated by Django 4.1 on 2022-08-24 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs1', '0006_commentreply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentreply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_to_comment', to='blogs1.blogcomment'),
        ),
    ]
