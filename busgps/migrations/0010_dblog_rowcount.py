# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busgps', '0009_dblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='dblog',
            name='rowcount',
            field=models.IntegerField(null=True, verbose_name='\u884c\u6570'),
        ),
    ]
