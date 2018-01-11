#!/usr/bin/env python
import glob
import os

os.system('rm -rf /home/gyuanfan/2016/DM/data/DDSM_label_ori/')
os.system('mkdir /home/gyuanfan/2016/DM/data/DDSM_label_ori/')

for file in glob.glob("/home/gyuanfan/2016/DM/data/DDSM/cancers/*/case*"):
    string='python prepare_contour_perdir_ori.py '+file
    os.system(string)
