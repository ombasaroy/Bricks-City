# Generated by Django 3.2.25 on 2024-04-17 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrickCity', '0017_alter_mypost_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
    ]
