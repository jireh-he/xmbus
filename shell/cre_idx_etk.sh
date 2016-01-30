sqlplus myoracle/myoracle <<!
-- Create/Recreate indexes 
create index BUSGPS_XMGJ_ETK_2115706C on BUSGPS_XMGJ_ETK (JYSJ)
  tablespace DATATBS01
  pctfree 10
  initrans 2
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  );
create index BUSGPS_XMGJ_ETK_5BA0762F on BUSGPS_XMGJ_ETK (XLH)
  tablespace DATATBS01
  pctfree 10
  initrans 2
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  );
create index BUSGPS_XMGJ_ETK_BD34070F on BUSGPS_XMGJ_ETK (CPH)
  tablespace DATATBS01
  pctfree 10
  initrans 2
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  );
-- Create/Recreate primary, unique and foreign key constraints 
alter table BUSGPS_XMGJ_ETK
  add primary key (ID)
  using index 
  tablespace DATATBS01
  pctfree 10
  initrans 2
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  );
!
