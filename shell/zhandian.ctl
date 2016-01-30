LOAD DATA 
CHARACTERSET UTF8
INFILE 'zhandian.csv'
BADFILE 'bad_zhandian.bad' 
TRUNCATE INTO TABLE BUSGPS_ZHANDIAN
FIELDS TERMINATED BY ","
TRAILING NULLCOLS
(
id,
zhandianming,
shangxiaxing,
cnt,
jingdu "to_number(:jingdu)/1000000",
weidu "to_number(:weidu)/1000000",
bmaplng,
bmaplat "replace(:bmaplat,chr(13),'')"
)
