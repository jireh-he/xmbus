# -*- coding: utf-8 -*-
# 查询列表中某站点名的元素，进行增删改
class StationSearch(object):
    def __init__(self, lsArray=[], zdm=''):
        self.lsArray = lsArray
        self.zdm = zdm.replace(u'︵', '(').replace(u'︶', ')')

    # 获得站点名对应的数组序号
    def __getzdmindex(self):
        if self.lsArray is None:
            return None
        idx = 0
        for ls in self.lsArray:
            if ls['zdm'] == self.zdm:
                return idx
            idx += 1
        return None

    # 获得途经站点的线路号列表
    def getxlhlist(self):
        idx = self.__getzdmindex()
        if idx is None:
            return None
        else:
            return self.lsArray[idx]['xlh']

    # 更新途经站点的线路号
    def updatezdm(self, xlh):
        idx = self.__getzdmindex()
        if idx is None:
            self.lsArray.append({"zdm": self.zdm, "xlh": xlh})
        else:
            self.lsArray[idx]['xlh'] = xlh
        return self.lsArray
