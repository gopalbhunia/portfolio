# Generated by Django 4.2 on 2023-04-16 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_projects'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
