from ljpeg import ljpeg
import glob, os
import re
import cv2
import numpy

#os.system('rm -rf /home/gyuanfan/2016/DM/data/DDSM_tif_ori')
#os.system('mkdir /home/gyuanfan/2016/DM/data/DDSM_tif_ori')

for file in glob.glob("/home/gyuanfan/2016/DM/data/DDSM/*/*/*/*LJPEG"):
    try:
        x = ljpeg.read(file).astype('uint16')
        X,Y=x.shape
        if(X>Y):
            pass
        else:
            x=x.reshape(Y,X)

        table=file.split('/')
        name=table[len(table)-1]
        name = re.sub("LJPEG","tif",name)
        tif="/home/gyuanfan/2016/DM/data/DDSM_tif_ori/"+name
        cv2.imwrite(tif,x)
        print(x.max(),x.min())
        x=cv2.imread(tif,-1)
        print(x.max(),x.min())

    except:
       print(file)
    break

