# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_time', models.DateTimeField(verbose_name=b'From:')),
                ('to_time', models.DateTimeField(verbose_name=b'To:')),
                ('reserved_by', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=200)),
                ('equipment', models.ForeignKey(to='rent.Equipment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
