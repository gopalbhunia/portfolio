# Generated by Django 4.2 on 2023-04-16 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_blogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=50)),
                ('projectDescription', models.TextField()),
                ('projectTimestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
