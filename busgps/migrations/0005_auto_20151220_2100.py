# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busgps', '0004_auto_20151220_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tab_linestations',
            name='qita',
            field=models.CharField(max_length=100, null=True, verbose_name='\u5176\u4ed6'),
        ),
    ]
