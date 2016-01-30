LOAD DATA CHARACTERSET ZHS16GBK 
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140501.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140502.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140503.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140504.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140505.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140506.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140507.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140508.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140509.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140510.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140511.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140512.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140513.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140514.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140515.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140516.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140517.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140518.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140519.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140520.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140521.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140522.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140523.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140524.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140525.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140526.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140527.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140528.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140529.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140530.txt'
INFILE '/mnt/hgfs/U/xmbus/txtdb/TAB_GPSINFODATA140531.txt'
BADFILE 'bad_gpsinfodata.bad'
TRUNCATE INTO TABLE BUSGPS_TAB_GPSINFODATA
FIELDS TERMINATED BY ","
TRAILING NULLCOLS
(
hisid, 
devidstr, 
stime "to_timestamp(:stime,'yyyy-mm-dd hh24:mi:ss')", 
gtime "to_timestamp(:gtime,'yyyy-mm-dd hh24:mi:ss.ff3')", 
atype, 
islocat, 
latitude "to_number(:latitude)/1000000", 
longtitude "to_number(:longtitude)/1000000", 
hight, 
speed, 
direction, 
s1, 
s2, 
s3, 
s4, 
isreplace, 
cartype, 
isstation, 
station_id, 
area_id, 
sumdis, 
busline_no
)

