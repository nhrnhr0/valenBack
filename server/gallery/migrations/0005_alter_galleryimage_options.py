# Generated by Django 4.1.5 on 2023-01-19 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_rename_exif_data_galleryimage_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryimage',
            options={'ordering': ['-created_at']},
        ),
    ]
