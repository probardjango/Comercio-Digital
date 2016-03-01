# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_producto_managers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='usuario',
            new_name='user',
        ),
    ]
