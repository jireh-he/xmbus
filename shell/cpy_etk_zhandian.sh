sqlplus myoracle/myoracle <<!
	set arraysize 500;
	set copycommit 500;
	set copytypecheck off;
	set long 100000;
	copy from myoracle/myoracle@myoracle to myoracle/myoracle@myoracle create busgps_etk_zhandian using select * from v_busgps_etk_zhandian;
!
