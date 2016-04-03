/**
 * Created by admin on 2016-2-18.
 */
var fetchPos=function(cityname){
    var myGeo = new BMap.Geocoder();
    var convertor = new BMap.Convertor();
    $("#bus_stops tbody tr").each(function(){
        var arrtd=$(this).children();
        myGeo.getPoint($.trim(arrtd.eq(0).text()+'-公交站'),function(point){
            if(point){
                arrtd.eq(2).text(point.lng);
                arrtd.eq(3).text(point.lat);
            }
            convertor.translate([point],1,5,function(data){
                newpoint=data.points[0];
                if(newpoint) {
                    x = 2 * point.lng - newpoint.lng;
                    y = 2 * point.lat - newpoint.lat;
                    arrtd.eq(4).text(x);
                    arrtd.eq(5).text(y);
                }
            });
        },cityname)
    });

};

var savPos=function(cityid){
    var jsondata=[]
    $("#bus_stops tbody tr").each(function() {
        var arrtd = $(this).children();
        jsondata.push([arrtd.eq(0).text(),arrtd.eq(1).text(),arrtd.eq(2).text(),arrtd.eq(3).text(),arrtd.eq(4).text(),arrtd.eq(5).text()]);

    });
    $.ajax(
        {
            'url': '/savepoints',
            'type':'POST',
            'data':{
                "jsondata":JSON.stringify(jsondata),
                'cityid':cityid
            },
            'success':function(res){
                if(res.message=='success'){
                    alert('更新成功');
                    window.location.reload();
                }
            },
            'error':function(res){
                var desc='';
                for(var i in res){
                    var pr=res[i];
                    desc+=i+'='+pr+'\n';
                }
                document.write(desc);
            }

        });
}