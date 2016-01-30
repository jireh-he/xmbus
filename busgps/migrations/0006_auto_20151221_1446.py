# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busgps', '0005_auto_20151220_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tab_gpsinfodata',
            name='devidstr',
            field=models.CharField(max_length=20, null=True, verbose_name='\u8bbe\u5907\u7f16\u53f7', db_index=True),
        ),
        migrations.AlterField(
            model_name='tab_gpsinfodata',
            name='gtime',
            field=models.DateTimeField(null=True, verbose_name='Gps\u65f6\u95f4', db_index=True),
        ),
        migrations.AlterField(
            model_name='tab_gpsinfodata',
            name='latitude',
            field=models.DecimalField(null=True, verbose_name='\u7eac\u5ea6', max_digits=10, decimal_places=6),
        ),
        migrations.AlterField(
            model_name='tab_gpsinfodata',
            name='longtitude',
            field=models.DecimalField(null=True, verbose_name='\u7ecf\u5ea6', max_digits=10, decimal_places=6),
        ),
        migrations.AlterField(
            model_name='tab_gpsinfodata',
            name='stime',
            field=models.DateTimeField(null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4'),
        ),
    ]
