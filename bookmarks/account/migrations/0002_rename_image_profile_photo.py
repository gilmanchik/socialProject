# Generated by Django 4.2.7 on 2023-11-17 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='photo',
        ),
    ]
