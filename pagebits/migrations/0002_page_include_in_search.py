# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagebits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='include_in_search',
            field=models.BooleanField(default=True),
        ),
    ]
