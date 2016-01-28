# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio_rebajas',
            field=models.DecimalField(default=6.99, max_digits=50, decimal_places=2),
        ),
    ]
