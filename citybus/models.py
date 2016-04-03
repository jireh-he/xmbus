# coding:utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class CityList(models.Model):
    cityname = models.CharField("城市名", max_length=100, default="厦门")
    cityurl = models.CharField("网页链接地址", max_length=500, null=True)
    cid=models.IntegerField('城市编号',null=True)

    def __str__(self):
        return self.cityname

    class Meta:
        verbose_name = '城市名'
        verbose_name_plural = '各大城市名称'
        db_table = 'cb_city'


class LineTypes(models.Model):
    typename = models.CharField('线路类型', max_length=100, default="")
    fetchurl = models.CharField("抓取的网页链接", max_length=500, null=True)
    city = models.ForeignKey(CityList, default=0)

    def __str__(self):
        return self.typename

    class Meta:
        verbose_name = '公交分类'
        verbose_name_plural = '各城市公交分类'
        db_table = 'cb_linetypes'

@python_2_unicode_compatible
class CityBusLines(models.Model):
    xlh = models.CharField('线路号', max_length=100, null=True,db_index=True)
    fetchurl = models.CharField('抓取的网页链接', max_length=500, null=True)
    yxsj=models.CharField('运行时间',max_length=1000,null=True)
    pjxx=models.CharField('票价信息',max_length=1000,null=True)
    gjgs=models.CharField('公交公司',max_length=100,null=True)
    sxfx=models.CharField('上行方向',max_length=100,null=True)
    xxfx=models.CharField('下行方向',max_length=100,null=True)
    city = models.ForeignKey(CityList, default=0)
    linetype=models.ForeignKey(LineTypes,default=0)

    def __str__(self):
        return self.xlh

    class Meta:
        verbose_name = '城市公交线路'
        verbose_name_plural = '各大城市公交线路信息表'
        db_table = 'cb_city_buslines'


@python_2_unicode_compatible
class CityBusStations(models.Model):
    zdm = models.CharField('站点名', max_length=50, null=True)
    updown = models.CharField('上下行_上0_下1', max_length=10, null=True)
    zdxh = models.IntegerField('站点序号', null=True)
    jingdu = models.DecimalField('经度', null=True, max_digits=10, decimal_places=6)
    weidu = models.DecimalField('纬度', null=True, max_digits=10, decimal_places=6)
    gpslng = models.DecimalField('GPS经度', null=True, max_digits=10, decimal_places=6)
    gpslat = models.DecimalField('GPS纬度', null=True, max_digits=10, decimal_places=6)
    busline=models.ForeignKey(CityBusLines,default=0)

    def __str__(self):
        return self.zdm

    class Meta:
        verbose_name = '城市公交站'
        verbose_name_plural = '各大城市公交站点信息表'
        db_table = 'cb_bus_stations'

