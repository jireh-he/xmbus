sqlplus myoracle/myoracle <<!
/*
create index ETK_ZHANDIAN_IDX on BUSGPS_ETK_ZHANDIAN(JYSJ,XLH,CHEPAIHAO)
  tablespace DATATBS01
  pctfree 10
  initrans 2
  maxtrans 255
  storage
  (
	initial 64k
        next 1M
        minextents 1
        maxextents unlimited
  );
*/
create index STATIONID_IDX on BUSGPS_ETK_ZHANDIAN(STATIONID,0)
  tablespace DATATBS01
  pctfree 10
  initrans 2
  maxtrans 255
  storage
  (
	initial 64k
        next 1M
        minextents 1
        maxextents unlimited
  );
!
