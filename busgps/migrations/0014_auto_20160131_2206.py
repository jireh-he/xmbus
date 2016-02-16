# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busgps', '0013_auto_20160131_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='bd_buslines',
            name='gpslat',
            field=models.DecimalField(null=True, verbose_name='GPS\u7eac\u5ea6', max_digits=10, decimal_places=6),
        ),
        migrations.AddField(
            model_name='bd_buslines',
            name='gpslng',
            field=models.DecimalField(null=True, verbose_name='GPS\u7ecf\u5ea6', max_digits=10, decimal_places=6),
        ),
    ]
