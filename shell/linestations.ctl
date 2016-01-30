LOAD DATA 
CHARACTERSET UTF8
INFILE '/mnt/hgfs/U/xmbus/txtdb/tab_linestations.txt'  
BADFILE 'bad_linestations.bad' 
TRUNCATE INTO TABLE BUSGPS_TAB_LINESTATIONS  
FIELDS TERMINATED BY ","
TRAILING NULLCOLS
(
id RECNUM,
xlh, 
zdm, 
updown, 
zdxh, 
jingdu "to_number(:jingdu)/1000000", 
weidu "to_number(:weidu)/1000000", 
qita
)
