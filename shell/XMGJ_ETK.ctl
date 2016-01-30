LOAD DATA 
CHARACTERSET ZHS16GBK 
INFILE '/mnt/hgfs/U/xmbus/txtdb/XMGJ_ETK_201405.txt'  
BADFILE 'bad_XMGJ_ETK.bad' 
APPEND INTO TABLE BUSGPS_XMGJ_ETK  
FIELDS TERMINATED BY ","
TRAILING NULLCOLS
(
gjgsdm, 
rksj, 
kahao "trim(:kahao)", 
jysj "trim(:jysj)", 
jyje, 
klx, 
xlh "trim(:xlh)", 
czzdbh, 
cph "replace(:cph,chr(13),'')",
ID RECNUM
)

