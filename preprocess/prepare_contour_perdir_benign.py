import glob
import re
import sys
import os
import os.path
import numpy as np
import cv2



row={}
column={}

for file in glob.glob(sys.argv[1]+"/*ics"):
    ICS=open(file,'r')
    for line in ICS:
        if ((re.search('^LEFT',line) is not None) or (re.search('^RIGHT',line) is not None)):
            table=line.split(" ")
            row[table[0]]=table[2]
            column[table[0]]=table[4]
    break

ICS.close()


## use LJPEG so that also generate negative examples here.
for file in glob.glob(sys.argv[1]+"/*LJPEG"):
    name = re.sub("LJPEG","OVERLAY",file)
    print(name)
    namelist=name.split('.')
    print(namelist[1])
    b=np.zeros([int(row[namelist[1]]),int(column[namelist[1]])])

    if os.path.isfile(name):
        print "tumor identified"
        num_lines = sum(1 for line in open(name))
        LABEL=open(name,'r')
        line_i=0
        while (line_i<num_lines):
            line=LABEL.readline()
            line_i+=1
            if (re.search('PATHOLOGY BENIGN',line) is not None):
                while (re.search('BOUNDARY', line) is None):
                    line=LABEL.readline()
                    line_i+=1
                    pass
                line=LABEL.readline()
                line=re.sub('  ',' ',line)
                line_i+=1
                #print(line)
                location=line.split(' ')
                i_tmp=0
                x=int(location[i_tmp])
                i_tmp+=1
                y=int(location[i_tmp])
                polygon=[]
                while (i_tmp<(len(location)-1)):
                    if (int(location[i_tmp])==0):
                        x=x
                        y=y-1
                        polygon.append([x,y])
                        pass
                    if (int(location[i_tmp])==1):
                        x=x+1
                        y=y-1
                        polygon.append([x,y])
                        pass
                    if (int(location[i_tmp])==2):
                        x=x+1
                        y=y
                        polygon.append([x,y])
                        pass
                    if (int(location[i_tmp])==3):
                        x=x+1
                        y=y+1
                        polygon.append([x,y])
                        pass
                    if (int(location[i_tmp])==4):
                        x=x
                        y=y+1
                        polygon.append([x,y])
                        pass
                    if (int(location[i_tmp])==5):
                        x=x-1
                        y=y+1
                        polygon.append([x,y])
                        pass
                    if (int(location[i_tmp])==6):
                        x=x-1
                        y=y
                        polygon.append([x,y])
                        pass
                    if (int(location[i_tmp])==7):
                        x=x-1
                        y=y-1
                        polygon.append([x,y])
                        pass
                    i_tmp+=1

                #print(polygon)
                poly = np.array(polygon, dtype=np.int32)
                #print(poly)
                #print(poly.shape)
                cv2.fillPoly(b, [poly], 255)
                print('deadafter')
            pass
    else:
        print "no tumor present"

    #b=cv2.resize(b,None,None,0.2,0.2)

    name = re.sub("LJPEG","tif",file)
    fullnamelist=name.split('/')
    c=cv2.imread('/home/gyuanfan/2016/DM/data/DDSM_tif_ori/'+fullnamelist[len(fullnamelist)-1],-1)
    [x1,y1]=c.shape
    [x2,y2]=b.shape
    print(x1,x2,y1,y2)
    if ((x1 == x2) and (y1== y2)):
        newname='/home/gyuanfan/2016/DM/data/DDSM_benign_label_ori/'+fullnamelist[len(fullnamelist)-1]
        if (b.max()>0):
            cv2.imwrite(newname,b)
            aaa=cv2.imread(newname,-1);
            print(aaa.shape)
#        break


