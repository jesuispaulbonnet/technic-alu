# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-09 15:01
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_presentationblock'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='presentation_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
