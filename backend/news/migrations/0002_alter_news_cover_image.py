# Generated by Django 3.2.6 on 2021-08-08 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='cover_image',
            field=models.ImageField(upload_to='static/img/cover_images'),
        ),
    ]
