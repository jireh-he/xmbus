sqlldr myoracle/myoracle@myoracle control=tab_gpsbuslines.txt.ctl skip=0  rows=100000 errors=10000 bindsize=16384000 readsize=16384000 log=log_tab_gpsbuslines.txt.log bad=bad_tab_gpsbuslines.txt.bad
