# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-31 07:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.TextField(max_length=50)),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Roti',
            fields=[
                ('menu_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='webpage_display.Menu')),
            ],
            bases=('webpage_display.menu',),
        ),
    ]
