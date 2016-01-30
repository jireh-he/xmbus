#去掉BUSGPS_XMGJ_ETK表中CPH字段中的chr(13)，回车键
sqlplus myoracle/myoracle <<!
	UPDATE /*+ PARALLEL(BUSGPS_XMGJ_ETK,4) */ BUSGPS_XMGJ_ETK SET CPH=REPLACE(CPH,CHR(13),'');
	COMMIT; 
!
