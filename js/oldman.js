/**
 * Created by admin on 2016-3-11.
 */
//提示标签
var tooltip=d3.select("body").append("div")
    .attr("class","tooltip")
    .style('opacity',0.0);
var groups,xScale,yScale,xAxis,yAxis;
//初始自适应大小
var w=window,d=document,e= d.documentElement,
    width=(w.innerWidth || e.clientWidth || g.clientWidth)*0.8,
    height= w.innerHeight|| e.clientHeight|| g.clientHeight;
    margin = {top: 30, right : 20, bottom: 80, left: 50};
var svg = d3.select("#totalshow").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom);
//颜色比例尺
var color=d3.scale.category10();
var names=["刷卡人次","出行人数","老人刷卡次数","老人出行人数"];
d3.json("/static/newjs/oldman.json", function(error, data) {
  if (error) return console.warn(error);
  drawLegend(color,data.dataset);
  drawStack(data.dataset);

});

function drawStack(jsondata){

    var stack=d3.layout.stack()
        .offset("zero")
        .values(function(d){return d.cnt})
        .x(function(d){return d.riqi})
        .y(function(d){return d.num});

    var data=stack(jsondata);

    var xRangeWidth=width-margin.left-margin.right;
    xScale= d3.scale.ordinal()
        .domain(data[0].cnt.map(function(d){return d.riqi;}))
        .rangeRoundBands([0,xRangeWidth],0.1);
    var yRangeHeight=height-margin.top-margin.bottom;

    //添加分组元素
    svg.selectAll("g").remove();
	groups = svg.selectAll("g")
					.data(data)
					.enter()
					.append("g")
					.style("fill",function(d,i){ return color(i); })
                    .filter(function(g,i){
                        var chk=d3.select("input[value='"+i+"']").property("checked");
                        return chk;});
    var numlist=d3.merge(groups.data().map(function(m){return m.cnt.map(function(d){return d.y})}));
    var maxnum=d3.max(numlist,function(m){return parseInt(m);});
    yScale=d3.scale.linear()
        .domain([0,maxnum])  //定义域
        .range([yRangeHeight,0]); //值域

    //添加矩形
    var rects=groups.selectAll("rect")
        .data(function(d){return d.cnt;})
        .enter()
        .append("rect")
        .attr("width",xScale.rangeBand())
        .attr("x",function(d){return xScale(d.riqi)})
        .attr("y",function(d){return yScale(d.y)})
        .attr("height",function(d){
            return yScale(0)-yScale(d.y);
        })
        .attr("transform","translate(" + margin.left + "," + (height - margin.bottom-yRangeHeight) +  ")")
        .on("mouseover",function(d){
          tooltip.html(d.y).style("left", (d3.event.pageX) + "px")
              .style("top", (d3.event.pageY + 20) + "px")
              .style("opacity",1.0);
      })
      .on("mousemove",function(d){
            /* 鼠标移动时，更改样式 left 和 top 来改变提示框的位置 */
            tooltip.style("left", (d3.event.pageX) + "px")
            .style("top", (d3.event.pageY + 20) + "px");
      })
      .on("mouseout",function(d){
        /* 鼠标移出时，将透明度设定为0.0（完全透明）*/
        tooltip.style("opacity",0.0);
      })

    //添加坐标轴
    xAxis=d3.svg.axis()
        .scale(xScale).orient("bottom");
    yAxis = d3.svg.axis()
					.scale(yScale)
					.orient("left")
        .tickFormat(d3.format(".2s"));

    svg.append("g")
			.attr("class","x axis")
			.attr("transform","translate(" + margin.left + "," + (height-margin.bottom) +  ")")
			.call(xAxis)
            .selectAll("text")
            .attr("x",40)
            .attr("y",-5)
            .attr("transform","rotate(90)");

	svg.append("g")
			.attr("class","y axis")
			.attr("transform","translate(" + margin.left + "," + (height - margin.bottom - yRangeHeight) +  ")")
			.call(yAxis)
            .append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .text("人次或人数");



}
//添加分组图例标签
function drawLegend(color,jsondata){

    var legend = d3.select("#totalshow").insert("div","svg")
    .attr("class","legend")
    .selectAll("label")
    .data(jsondata)
    .enter().append("label")
    .attr("class","checkbox-inline")
    .html(function(d,i){
    return "<input type='checkbox' value='"+i+"' checked >"+ d.name;
    })
    .style("background-color",function(d,i){return color(i)})
    .style("left",margin.left+"px")
        .selectAll("input")
        .on("change",function(){
            drawStack(jsondata);
        });
}



