# Generated by Django 4.2.4 on 2023-09-06 22:28

from django.db import migrations
import wagtail.fields
import wagtailmarkdown.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='markdown',
            field=wagtailmarkdown.fields.MarkdownField(blank=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
