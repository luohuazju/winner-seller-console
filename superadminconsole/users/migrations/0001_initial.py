# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=128)),
                ('create_date', models.DateTimeField(verbose_name=b'Create Date')),
                ('update_date', models.DateTimeField(verbose_name=b'Update Date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
                ('create_date', models.DateTimeField(verbose_name=b'Create Date')),
                ('update_date', models.DateTimeField(verbose_name=b'Update Date')),
                ('roles', models.ManyToManyField(to='users.Role')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
