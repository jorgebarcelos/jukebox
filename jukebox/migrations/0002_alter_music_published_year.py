# Generated by Django 3.2.16 on 2023-02-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jukebox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='published_year',
            field=models.CharField(max_length=20),
        ),
    ]
