# Generated by Django 3.2.25 on 2024-04-17 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BrickCity', '0014_auto_20240417_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='quote',
        ),
        migrations.RemoveField(
            model_name='post',
            name='thumbnail',
        ),
    ]