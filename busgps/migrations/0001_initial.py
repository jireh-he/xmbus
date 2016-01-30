# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tab_gpsbuslines',
            fields=[
                ('fenzuming', models.CharField(max_length=50, null=True, verbose_name='\u5206\u7ec4\u540d')),
                ('xianluhao', models.CharField(max_length=50, null=True, verbose_name='\u7ebf\u8def\u53f7')),
                ('chepaihao', models.CharField(serialize=False, max_length=50, null=True, verbose_name='\u8f66\u724c\u53f7', primary_key=True)),
                ('shebeiID', models.CharField(max_length=50, null=True, verbose_name='\u8bbe\u5907ID')),
                ('simkahao', models.CharField(max_length=50, null=True, verbose_name='SIM\u5361\u53f7')),
            ],
            options={
                'db_table': 'busgps_tab_gpsbuslines',
                'verbose_name': '\u516c\u4ea4\u8f66GPS\u8bbe\u5907',
                'verbose_name_plural': '\u516c\u4ea4\u8f66GPS\u8bbe\u5907\u5bf9\u5e94\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='Tab_gpsinfodata',
            fields=[
                ('hisid', models.IntegerField(default=0, serialize=False, verbose_name='\u8bb0\u5f55ID\u53f7', primary_key=True)),
                ('devidstr', models.CharField(max_length=20, null=True, verbose_name='\u8bbe\u5907\u7f16\u53f7')),
                ('stime', models.CharField(max_length=2, null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('gtime', models.CharField(max_length=2, null=True, verbose_name='Gps\u65f6\u95f4')),
                ('atype', models.IntegerField(null=True, verbose_name='atype')),
                ('islocat', models.IntegerField(null=True, verbose_name='islocat')),
                ('latitude', models.FloatField(null=True, verbose_name='\u7eac\u5ea6')),
                ('longtitude', models.FloatField(null=True, verbose_name='\u7ecf\u5ea6')),
                ('hight', models.IntegerField(null=True, verbose_name='\u9ad8\u5ea6')),
                ('speed', models.IntegerField(null=True, verbose_name='\u901f\u5ea6')),
                ('direction', models.IntegerField(null=True, verbose_name='\u65b9\u5411')),
                ('s1', models.IntegerField(null=True, verbose_name='S1')),
                ('s2', models.IntegerField(null=True, verbose_name='S2')),
                ('s3', models.IntegerField(null=True, verbose_name='S3')),
                ('s4', models.IntegerField(null=True, verbose_name='S4')),
                ('isreplace', models.IntegerField(null=True, verbose_name='\u662f\u5426\u66ff\u6362')),
                ('station_id', models.IntegerField(null=True, verbose_name='\u7ad9\u70b9id')),
                ('area_id', models.IntegerField(null=True, verbose_name='\u533a\u57df\u7f16\u53f7')),
                ('sumdis', models.IntegerField(null=True, verbose_name='sumdis')),
                ('busline_no', models.CharField(max_length=20, null=True, verbose_name='\u516c\u4ea4\u7ebf\u8def\u53f7')),
            ],
            options={
                'db_table': 'busgps_tab_gpsinfodata',
                'verbose_name': '\u516c\u4ea4GPS\u5b9a\u4f4d',
                'verbose_name_plural': '\u516c\u4ea4GPS\u5b9a\u4f4d\u5386\u53f2\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='Tab_linestations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('xlh', models.CharField(max_length=20, null=True, verbose_name='\u7ebf\u8def\u53f7')),
                ('zdm', models.CharField(max_length=50, null=True, verbose_name='\u7ad9\u70b9\u540d')),
                ('updown', models.CharField(max_length=10, null=True, verbose_name='\u4e0a\u4e0b\u884c_\u4e0a0_\u4e0b1')),
                ('zdxh', models.CharField(max_length=10, null=True, verbose_name='\u7ad9\u70b9\u5e8f\u53f7')),
                ('jingdu', models.CharField(max_length=30, null=True, verbose_name='\u7ecf\u5ea6')),
                ('weidu', models.CharField(max_length=30, null=True, verbose_name='\u7eac\u5ea6')),
                ('qita', models.TextField(null=True, verbose_name='\u5176\u4ed6')),
            ],
            options={
                'db_table': 'busgps_tab_linestations',
                'verbose_name': '\u516c\u4ea4\u7ebf\u8def\u7ad9\u70b9',
                'verbose_name_plural': '\u516c\u4ea4\u7ebf\u8def\u7ad9\u70b9\u4fe1\u606f\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='Xmgj_cardtype',
            fields=[
                ('cardtypeid', models.CharField(max_length=20, serialize=False, verbose_name='\u5361\u7c7b\u578b\u7f16\u53f7', primary_key=True)),
                ('cardtypename', models.CharField(max_length=50, verbose_name='\u5361\u7c7b\u578b\u540d\u79f0')),
            ],
            options={
                'db_table': 'busgps_xmgj_cardtype',
                'verbose_name': '\u516c\u4ea4\u5361\u7c7b\u578b',
                'verbose_name_plural': '\u516c\u4ea4\u5361\u7c7b\u578b\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='Xmgj_company',
            fields=[
                ('companyid', models.CharField(max_length=20, serialize=False, verbose_name='\u516c\u53f8\u7f16\u53f7', primary_key=True)),
                ('companyname', models.CharField(max_length=50, null=True, verbose_name='\u516c\u53f8\u540d\u79f0')),
            ],
            options={
                'db_table': 'busgps_xmgj_company',
                'verbose_name': '\u516c\u4ea4\u516c\u53f8',
                'verbose_name_plural': '\u516c\u4ea4\u516c\u53f8\u540d\u79f0\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='Xmgj_etk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gjgsdm', models.CharField(max_length=11, null=True, verbose_name='\u516c\u4ea4\u516c\u53f8\u4ee3\u7801')),
                ('rksj', models.CharField(max_length=14, null=True, verbose_name='\u5165\u5e93\u65f6\u95f4')),
                ('kahao', models.CharField(max_length=19, null=True, verbose_name='\u5361\u53f7')),
                ('jysj', models.CharField(max_length=14, null=True, verbose_name='\u4ea4\u6613\u65f6\u95f4', db_index=True)),
                ('jyje', models.CharField(max_length=10, null=True, verbose_name='\u4ea4\u6613\u91d1\u989d')),
                ('klx', models.CharField(max_length=6, null=True, verbose_name='\u5361\u7c7b\u578b')),
                ('xlh', models.CharField(max_length=6, null=True, verbose_name='\u7ebf\u8def\u53f7', db_index=True)),
                ('czzdbh', models.CharField(max_length=8, null=True, verbose_name='\u8f66\u8f7d\u7ec8\u7aef\u7f16\u53f7')),
                ('cph', models.CharField(max_length=10, null=True, verbose_name='\u8f66\u724c\u53f7', db_index=True)),
            ],
            options={
                'db_table': 'busgps_xmgj_etk',
                'verbose_name': 'E\u901a\u5361',
                'verbose_name_plural': '\u53a6\u95e8\u516c\u4ea4E\u901a\u5361\u5237\u5361\u8bb0\u5f55',
            },
        ),
    ]
