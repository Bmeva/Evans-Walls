# Generated by Django 5.0.3 on 2024-04-14 14:02

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_alter_blog_blog_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_body',
            field=tinymce.models.HTMLField(),
        ),
    ]
