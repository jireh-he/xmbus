# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busgps', '0002_auto_20151220_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tab_gpsinfodata',
            name='gtime',
            field=models.CharField(max_length=30, null=True, verbose_name='Gps\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='tab_gpsinfodata',
            name='stime',
            field=models.CharField(max_length=30, null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4'),
        ),
    ]
