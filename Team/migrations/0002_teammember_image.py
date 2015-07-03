# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='image',
            field=models.ImageField(null=True, upload_to=b'team/'),
        ),
    ]
