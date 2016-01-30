sqlplus myoracle/myoracle <<!
 alter session enable parallel dml;
 alter table BUSGPS_ETK_ZHANDIAN nologging;
update/*+ parallel(t,4) */ BUSGPS_ETK_ZHANDIAN t
set t.stationid=(select nvl(z.stationid,0) from BUSGPS_ETK_ZHANDIAN z
where z.jysj>substr(t.jysj,1,12)||'00' and z.jysj<substr(t.jysj,1,12)||'59'
and z.chepaihao=t.chepaihao and z.xlh=t.xlh and z.stationid>0 and rownum=1)
where
t.stationid=0;
commit;
!
