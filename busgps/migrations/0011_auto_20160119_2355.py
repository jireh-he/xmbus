# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busgps', '0010_dblog_rowcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tab_linestations',
            name='jingdu',
            field=models.DecimalField(null=True, verbose_name='\u7ecf\u5ea6', max_digits=10, decimal_places=6),
        ),
        migrations.AlterField(
            model_name='tab_linestations',
            name='weidu',
            field=models.DecimalField(null=True, verbose_name='\u7eac\u5ea6', max_digits=10, decimal_places=6),
        ),
    ]
