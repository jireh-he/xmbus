$(function(){

	$("#downline").click(function(){
		for(var j=0;j<lines.length;j++)
		{
		var l=lines[j].replace(/\b(0+)/gi,"");
		showBusLine(l);
		}
		});
	$("#showbtn").click(function(){
		loadData();
		});
    $("#savebtn").click(function(){saveData();});
});
var showBusLine=function(xianluhao){
	if(!xianluhao)
		return false;
	var busline = new BMap.BusLineSearch('厦门',{
			onGetBusListComplete: function(result){
			   if(result) {
				 var fstLine = result.getBusListItem(1);//获取第一个公交列表显示到map上
				 busline.getBusLine(fstLine);
				 
			   }
			},
			onGetBusLineComplete:function(bl){
				var len=bl.getNumBusStations();
		
				var buslist=$('body').data('bus');
				if(!buslist)
					buslist=[];		
				for(var k=0;k<len;k++)
				{
					var bs=bl.getBusStation(k);
					var columns=[];
					columns.push(xianluhao);
					columns.push(bs.name);
					columns.push(bs.position.lng);
					columns.push(bs.position.lat);
					columns.push(k);
					buslist.push(columns);
				}
				$('body').data('bus',buslist);

			}
	});

	function busSearch(){
		
		busline.getBusList(xianluhao);
	}
	setTimeout(function(){
		busSearch();
	
	},1500);
};
var loadData=function(){
		 	
   	var dataset=$('body').data('bus');
   
   	if(dataset==undefined)
   	{
   		return 0;
   	}
   	
   	$("#showbus").html('');
   	$("#showbus").append("<table id='tableshow'></table>");
   	$("#tableshow").addClass("table table-striped table-hover");
   	var columns=[];
   	columns.push({"title":"线路号"});
   	columns.push({"title":"站点名"});
   	columns.push({"title":"经度"});
   	columns.push({"title":"纬度"});
	columns.push({"title":"站点序号"});
 
   	$("#tableshow").dataTable({
   		"data":dataset,
   		"columns":columns,
   	});
}; 

var saveData=function(){
    var dataset=$('body').data('bus');
    $.ajax({
        dataType:'json',
        url:'/savebus',
        method:'POST',
        data:{
			"bsdata":dataset,
		},
        success:function(res){
            $("#showbus").html('成功导入'+res.cnt+'条记录');

        },
    });
}
