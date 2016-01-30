sqlplus myoracle/myoracle <<!
execute dbms_stats.gather_table_stats(ownname=>'MYORACLE',tabname=>'BUSGPS_XMGJ_ETK');
!
