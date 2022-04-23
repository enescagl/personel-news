# Generated by Django 3.2.12 on 2022-04-07 21:06

import base.model_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_article_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=base.model_fields.SanitizedTextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='heading',
            field=base.model_fields.SanitizedCharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='article',
            name='short_description',
            field=base.model_fields.SanitizedCharField(max_length=256),
        ),
    ]
