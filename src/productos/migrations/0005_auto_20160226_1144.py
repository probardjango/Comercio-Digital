# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_producto_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='slug',
            field=models.SlugField(unique=True, blank=True),
        ),
    ]
