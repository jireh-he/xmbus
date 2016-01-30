# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busgps', '0011_auto_20160119_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bd_Buslines',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('xlh', models.CharField(max_length=20, null=True, verbose_name='\u7ebf\u8def\u53f7')),
                ('zdm', models.CharField(max_length=50, null=True, verbose_name='\u7ad9\u70b9\u540d')),
                ('updown', models.CharField(max_length=10, null=True, verbose_name='\u4e0a\u4e0b\u884c_\u4e0a0_\u4e0b1')),
                ('zdxh', models.CharField(max_length=10, null=True, verbose_name='\u7ad9\u70b9\u5e8f\u53f7')),
                ('jingdu', models.DecimalField(null=True, verbose_name='\u7ecf\u5ea6', max_digits=10, decimal_places=6)),
                ('weidu', models.DecimalField(null=True, verbose_name='\u7eac\u5ea6', max_digits=10, decimal_places=6)),
                ('qita', models.CharField(max_length=100, null=True, verbose_name='\u5176\u4ed6')),
            ],
            options={
                'db_table': 'busgps_bd_buslines',
                'verbose_name': '\u767e\u5ea6\u516c\u4ea4\u7ebf\u8def\u7ad9\u70b9',
                'verbose_name_plural': '\u516c\u4ea4\u7ebf\u8def\u7ad9\u70b9\u4fe1\u606f\u5217\u8868',
            },
        ),
    ]
