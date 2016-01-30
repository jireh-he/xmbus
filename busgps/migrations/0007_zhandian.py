# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busgps', '0006_auto_20151221_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zhandian',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zhandianming', models.CharField(max_length=50, null=True, verbose_name='\u7ad9\u70b9\u540d')),
                ('shangxiaxing', models.IntegerField(null=True, verbose_name='\u4e0a\u4e0b\u884c\u6807\u5fd7')),
                ('cnt', models.IntegerField(default=0, verbose_name='\u9014\u7ecf\u7ad9\u70b9\u7ebf\u8def\u6570')),
                ('jingdu', models.DecimalField(null=True, verbose_name='\u7ecf\u5ea6', max_digits=10, decimal_places=6)),
                ('weidu', models.DecimalField(null=True, verbose_name='\u7eac\u5ea6', max_digits=10, decimal_places=6)),
                ('bmaplng', models.DecimalField(null=True, verbose_name='\u767e\u5ea6\u7ecf\u5ea6', max_digits=10, decimal_places=6)),
                ('bmaplat', models.DecimalField(null=True, verbose_name='\u767e\u5ea6\u7eac\u5ea6', max_digits=10, decimal_places=6)),
            ],
            options={
                'db_table': 'busgps_zhandian',
                'verbose_name': '\u7ad9\u70b9\u5750\u6807',
                'verbose_name_plural': '\u516c\u4ea4\u7ad9\u70b9GPS\u5750\u6807\u5217\u8868',
            },
        ),
    ]
