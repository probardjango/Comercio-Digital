# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productos', '0008_producto_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='managers',
            field=models.ManyToManyField(related_name='managers_productos', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
