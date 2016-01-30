# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busgps', '0003_auto_20151220_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='tab_gpsinfodata',
            name='cartype',
            field=models.IntegerField(null=True, verbose_name='\u5361\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='tab_gpsinfodata',
            name='isstation',
            field=models.IntegerField(null=True, verbose_name='\u662f\u5426\u5230\u7ad9'),
        ),
    ]
