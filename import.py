#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xmbus.settings")

def importData(fdir):
    from busgps.models import Xmgj_etk
    EtkList=[]
    forloop=0
    file_object=open(fdir,'r')
    for line in file_object:
        forloop +=1
	line=line.strip('\n')
	parts=line.split(',')
	EtkList.append(Xmgj_etk(gjgsdm=parts[0],
			rksj=parts[1],
			kahao=parts[2],
			jysj=parts[3],
			jyje=parts[4],
			klx=parts[5],
			xlh=parts[6],
			czzdbh=parts[7],
			cph=parts[8]))
	if(forloop%10000==0):
		Xmgj_etk.objects.bulk_create(EtkList)
		EtkList=[]
        if(forloop >20000):
		break
 
def main():
    f = open('filelist.txt')
    for fdir in f:
	importData(fdir.strip('\n'))
    f.close()
     
 
if __name__ == "__main__":
    main()
    print('Done!')
