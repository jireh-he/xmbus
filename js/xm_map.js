/**
 * Created by admin on 2016-3-29.
 */

var map=new BMap.Map("map1");
$("#map1").width(width*0.8).height(height *0.9);
map.centerAndZoom("厦门",12);
map.enableScrollWheelZoom(true);
map.enablePinchToZoom(true);
$.getJSON("js/heat.json",function(data){
  var points=data;
  if(!isSupportCanvas()){
    	alert('热力图目前只支持有canvas支持的浏览器,您所使用的浏览器不能使用热力图功能~')
    }
	var mapv=new Mapv({drawTypeControl: true,map:map});
    // 创建一个图层
var layer = new Mapv.Layer({
    zIndex: 3, // 图层的层级
    mapv: mapv, // 对应的mapv
    dataType: 'point', // 数据类型，point:点数据类型,polyline:线数据类型,polygon:面数据类型
    //数据，格式如下
    data: points,
    drawType: 'density', // 展示形式
    // 渲染数据参数
    drawOptions: {
        type: "honeycomb", // 网格类型，方形网格或蜂窝形
        size: 30, // 网格大小
        globalAlpha: 0.6,
        unit: 'px', // 单位
        label: { // 是否显示文字标签
            show: true,
        },
        gradient: { // 显示的颜色渐变范围
            '0': 'blue',
            '0.6': 'cyan',
            '0.7': 'lime',
            '0.8': 'yellow',
            '1.0': 'red'
        },
        events: {
            click: function(e, data) {
                //console.log('click', e.point, data);
                var geoc = new BMap.Geocoder();
                geoc.getLocation(e.point, function (rs) {
                    var addComp = rs.addressComponents;
                    alert(addComp.province + ", " + addComp.city + ", " + addComp.district + ", " + addComp.street );
                });
            },
        }
    }
});
	//判断浏览区是否支持canvas
    function isSupportCanvas() {
     var elem = document.createElement('canvas');
     return !!(elem.getContext && elem.getContext('2d'));
    }

});

