# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_auto_20160226_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='slug',
            field=models.SlugField(unique=True, blank=True),
        ),
    ]
