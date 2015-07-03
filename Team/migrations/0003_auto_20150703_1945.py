# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Team', '0002_teammember_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='image',
            field=models.ImageField(default=b'', null=True, upload_to=b'team/'),
        ),
    ]
