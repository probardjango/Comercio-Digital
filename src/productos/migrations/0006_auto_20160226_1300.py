# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20160226_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
