# Generated by Django 4.2.4 on 2023-09-06 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpage_markdown_alter_blogpage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='markdown',
        ),
    ]
