# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busgps', '0008_auto_20151225_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dblog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tablename', models.CharField(max_length=50, verbose_name='\u8868\u540d')),
                ('flagField', models.CharField(max_length=100, null=True, verbose_name='\u6807\u5fd7\u5b57\u6bb5')),
                ('startTime', models.DateTimeField(null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('endTime', models.DateTimeField(null=True, verbose_name='\u7ed3\u675f\u65f6\u95f4')),
            ],
            options={
                'db_table': 'busgps_dblog',
                'verbose_name': '\u6570\u636e\u5e93\u64cd\u4f5c\u65e5\u5fd7',
                'verbose_name_plural': '\u6570\u636e\u5e93\u64cd\u4f5c\u65e5\u5fd7',
            },
        ),
    ]
