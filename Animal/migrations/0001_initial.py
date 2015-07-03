# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adopt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(default=b'', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('breed', models.CharField(default=b'', max_length=50)),
                ('age', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(default=b'', null=True, upload_to=b'team/')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(default=b'', max_length=500)),
                ('animal', models.OneToOneField(to='Animal.Animal')),
            ],
        ),
        migrations.AddField(
            model_name='adopt',
            name='animal',
            field=models.OneToOneField(to='Animal.Animal'),
        ),
    ]
