# Generated by Django 3.2.25 on 2024-05-03 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrickCity', '0023_auto_20240503_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='adverts/'),
        ),
    ]
