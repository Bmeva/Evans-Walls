# Generated by Django 5.0.3 on 2024-04-14 15:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_alter_blog_blog_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
