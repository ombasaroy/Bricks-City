# Generated by Django 4.2.13 on 2024-05-09 12:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrickCity', '0035_auto_20240507_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mypost',
            name='intro',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
