# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_precio_rebajas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio_rebajas',
            field=models.DecimalField(default=6.99, null=True, max_digits=50, decimal_places=2, blank=True),
        ),
    ]
