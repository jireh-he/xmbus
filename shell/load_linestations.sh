SET NLS_LANG=AMERICAN_AMERICA.AL32UTF8
sqlldr myoracle/myoracle@myoracle control=linestations.ctl skip=0 rows=50000  log=linestations.log direct=true
