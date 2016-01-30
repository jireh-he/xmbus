# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busgps', '0007_zhandian'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zhandian',
            name='bmaplat',
            field=models.DecimalField(null=True, verbose_name='\u767e\u5ea6\u7eac\u5ea6', max_digits=11, decimal_places=7),
        ),
        migrations.AlterField(
            model_name='zhandian',
            name='bmaplng',
            field=models.DecimalField(null=True, verbose_name='\u767e\u5ea6\u7ecf\u5ea6', max_digits=11, decimal_places=7),
        ),
    ]
