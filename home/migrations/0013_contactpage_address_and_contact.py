# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-23 12:33
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20180223_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='address_and_contact',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
