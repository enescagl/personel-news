# Generated by Django 3.2.12 on 2022-04-11 09:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_add_sanitized_model_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='article_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='deleted_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='article',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='article_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='imagecontent',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='imagecontent_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='imagecontent',
            name='deleted_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='imagecontent',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='imagecontent_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
