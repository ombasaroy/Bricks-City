# Generated by Django 3.2.25 on 2024-04-16 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BrickCity', '0007_auto_20240416_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thumbnail',
        ),
    ]
