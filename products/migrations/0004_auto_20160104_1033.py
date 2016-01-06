# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='sel_price',
            new_name='sale_price',
        ),
    ]
