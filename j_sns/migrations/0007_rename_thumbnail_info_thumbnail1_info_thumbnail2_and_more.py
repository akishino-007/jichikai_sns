# Generated by Django 5.1.2 on 2025-05-25 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('j_sns', '0006_info_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='thumbnail',
            new_name='thumbnail1',
        ),
        migrations.AddField(
            model_name='info',
            name='thumbnail2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='info',
            name='thumbnail3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
