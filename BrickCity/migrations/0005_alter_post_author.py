# Generated by Django 3.2.23 on 2024-04-12 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrickCity', '0004_auto_20240413_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, default='Admin', max_length=50, null=True),
        ),
    ]
