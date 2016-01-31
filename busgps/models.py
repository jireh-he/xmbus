#coding:utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Xmgj_etk(models.Model):
	gjgsdm=models.CharField('公交公司代码',max_length=11,null=True)
	rksj=models.CharField('入库时间',max_length=14,null=True)
	kahao=models.CharField('卡号',max_length=19,null=True)
	jysj=models.CharField('交易时间',max_length=14,null=True,db_index=True)
	jyje=models.CharField('交易金额',max_length=10,null=True)
	klx=models.CharField('卡类型',max_length=6,null=True)
	xlh=models.CharField('线路号',max_length=6,null=True,db_index=True)
	czzdbh=models.CharField('车载终端编号',max_length=8,null=True)
	cph=models.CharField('车牌号',max_length=10,null=True,db_index=True)

	def __str__(self):
		return self.cph

	class Meta:
		verbose_name='E通卡'
                verbose_name_plural='厦门公交E通卡刷卡记录'
                db_table='busgps_xmgj_etk'

@python_2_unicode_compatible
class Xmgj_company(models.Model):
	companyid=models.CharField('公司编号',max_length=20,primary_key=True)
	companyname=models.CharField('公司名称',max_length=50,null=True)

	def __str__(self):
		return self.companyname
	
	class Meta:
		verbose_name='公交公司'
		verbose_name_plural='公交公司名称列表'
		db_table='busgps_xmgj_company'

	
@python_2_unicode_compatible
class Xmgj_cardtype(models.Model):
	cardtypeid=models.CharField('卡类型编号',max_length=20,primary_key=True)
	cardtypename=models.CharField('卡类型名称',max_length=50)

	def __str__(self):
		return self.cardtypename

	class Meta:
		verbose_name='公交卡类型'
		verbose_name_plural='公交卡类型列表'
		db_table='busgps_xmgj_cardtype'


@python_2_unicode_compatible
class Tab_linestations(models.Model):
	xlh=models.CharField('线路号',max_length=20,null=True)
	zdm=models.CharField('站点名',max_length=50,null=True)
	updown=models.CharField('上下行_上0_下1',max_length=10,null=True)
	zdxh=models.CharField('站点序号',max_length=10,null=True)
	jingdu=models.DecimalField('经度',null=True,max_digits=10,decimal_places=6)
	weidu=models.DecimalField('纬度',null=True,max_digits=10,decimal_places=6)
	qita=models.CharField('其他',max_length=100,null=True)
	def __str__(self):
        	return self.zdm
	
	class Meta:
                verbose_name='公交线路站点'
                verbose_name_plural='公交线路站点信息列表'
                db_table='busgps_tab_linestations'


@python_2_unicode_compatible
class Tab_gpsinfodata(models.Model):
	hisid=models.IntegerField('记录ID号',default=0,primary_key=True)
	devidstr=models.CharField('设备编号',null=True,max_length=20,db_index=True)
	stime=models.DateTimeField('开始时间',null=True)
	gtime=models.DateTimeField('Gps时间',null=True,db_index=True)
	atype=models.IntegerField('atype',null=True)
	islocat=models.IntegerField('islocat',null=True)
	latitude=models.DecimalField('纬度',null=True,max_digits=10,decimal_places=6)
	longtitude=models.DecimalField('经度',null=True,max_digits=10,decimal_places=6)
	hight=models.IntegerField('高度',null=True)
	speed=models.IntegerField('速度',null=True)
	direction=models.IntegerField('方向',null=True)
	s1=models.IntegerField('S1',null=True)
	s2=models.IntegerField('S2',null=True)
	s3=models.IntegerField('S3',null=True)
	s4=models.IntegerField('S4',null=True)
	isreplace=models.IntegerField('是否替换',null=True)
	cartype=models.IntegerField('卡类型',null=True)
	isstation=models.IntegerField('是否到站',null=True)
	station_id=models.IntegerField('站点id',null=True)
	area_id=models.IntegerField('区域编号',null=True)
	sumdis=models.IntegerField('sumdis',null=True)
	busline_no=models.CharField('公交线路号',max_length=20,null=True)

        def __str__(self):
                return self.latitude+':'+self.longtitude

        class Meta:
                verbose_name='公交GPS定位'
                verbose_name_plural='公交GPS定位历史信息表'
                db_table='busgps_tab_gpsinfodata'

@python_2_unicode_compatible
class Tab_gpsbuslines(models.Model):
	fenzuming=models.CharField('分组名',null=True,max_length=50)
	xianluhao=models.CharField('线路号',null=True,max_length=50)
	chepaihao=models.CharField('车牌号',null=True,max_length=50,primary_key=True)
	shebeiID=models.CharField('设备ID',null=True,max_length=50)
	simkahao=models.CharField('SIM卡号',null=True,max_length=50)

	def __str__(self):
		return self.chepaihao

	class Meta:
		verbose_name='公交车GPS设备'
		verbose_name_plural='公交车GPS设备对应列表'
		db_table='busgps_tab_gpsbuslines'

@python_2_unicode_compatible
class Zhandian(models.Model):
	zhandianming=models.CharField('站点名',null=True,max_length=50)
	shangxiaxing=models.IntegerField('上下行标志',null=True)
	cnt=models.IntegerField('途经站点线路数',default=0)
	jingdu=models.DecimalField('经度',null=True,max_digits=10,decimal_places=6)
	weidu=models.DecimalField('纬度',null=True,max_digits=10,decimal_places=6)
	bmaplng=models.DecimalField('百度经度',null=True,max_digits=11,decimal_places=7)
	bmaplat=models.DecimalField('百度纬度',null=True,max_digits=11,decimal_places=7)
	def __str__(self):
		return self.zhandianming

	class Meta:
		verbose_name='站点坐标'
		verbose_name_plural='公交站点GPS坐标列表'
		db_table='busgps_zhandian'

@python_2_unicode_compatible
class Dblog(models.Model):
	tablename=models.CharField('表名',max_length=50)
	flagField=models.CharField('标志字段',max_length=100,null=True)
	startTime=models.DateTimeField('开始时间',null=True)
	endTime=models.DateTimeField('结束时间',null=True)
	rowcount=models.IntegerField('行数',null=True)
	
	def __str__(self):
		return self.tablename

	class Meta:
		verbose_name='数据库操作日志'
		verbose_name_plural='数据库操作日志'
		db_table='busgps_dblog'


@python_2_unicode_compatible
class Bd_Buslines(models.Model):
	xlh=models.CharField('线路号',max_length=20,null=True)
	zdm=models.CharField('站点名',max_length=50,null=True)
	updown=models.CharField('上下行_上0_下1',max_length=10,null=True)
	zdxh=models.IntegerField('站点序号',null=True)
	jingdu=models.DecimalField('经度',null=True,max_digits=10,decimal_places=6)
	weidu=models.DecimalField('纬度',null=True,max_digits=10,decimal_places=6)
	qita=models.CharField('其他',max_length=100,null=True)
	gpslng=models.DecimalField('GPS经度',null=True,max_digits=10,decimal_places=6)
	gpslat=models.DecimalField('GPS纬度',null=True,max_digits=10,decimal_places=6)
	def __str__(self):
        	return self.zdm
	
	class Meta:
                verbose_name='百度公交线路站点'
                verbose_name_plural='公交线路站点信息列表'
                db_table='busgps_bd_buslines'

