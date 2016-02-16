# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busgps', '0012_bd_buslines'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bd_buslines',
            name='zdxh',
            field=models.IntegerField(null=True, verbose_name='\u7ad9\u70b9\u5e8f\u53f7'),
        ),
    ]
