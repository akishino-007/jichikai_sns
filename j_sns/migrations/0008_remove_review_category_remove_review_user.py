# Generated by Django 5.1.2 on 2025-05-28 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('j_sns', '0007_rename_thumbnail_info_thumbnail1_info_thumbnail2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='category',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
    ]
