#!/usr/bin/env python
import glob
import os

os.system('rm -rf /home/gyuanfan/2016/DM/data/DDSM_benign_label_ori/')
os.system('mkdir /home/gyuanfan/2016/DM/data/DDSM_benign_label_ori/')
for file in glob.glob("/home/gyuanfan/2016/DM/data/DDSM/*/*/case*"):
    string='python prepare_contour_perdir_benign.py '+file
    os.system(string)
