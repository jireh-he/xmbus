sqlplus myoracle/myoracle <<!
create index GPSINFODATA_DEVIDSTR_IDX on BUSGPS_TAB_GPSINFODATA(DEVIDSTR)
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
