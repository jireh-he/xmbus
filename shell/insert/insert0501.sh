sqlplus myoracle/myoracle <<!
 alter session enable parallel dml; 
 alter table BUSGPS_ETK_ZHANDIAN nologging;
 insert /*+ parallel(t,4) +*/ into BUSGPS_ETK_ZHANDIAN t(KAHAO,JYSJ,KLX,XLH,CHEPAIHAO,SHEBEIID,STATIONID)
select KAHAO,JYSJ,KLX,XLH,CHEPAIHAO,SHEBEIID,STATIONID from V_BUSGPS_ETK_ZHANDIAN b where b.jysj like '20140501%';
	commit;
!
