# -*- coding: utf-8 -*-
"""
@author: guitar79@naver.com
#http://nmsc.kma.go.kr/emcoms/BIMG/COMS/Y2017/M08/D24/coms_mi_le1b_ir1_a_201708240545.png
"""
import urllib

Mon_list = ["01","02","03","04","05","06","07","08","09","10","11","12"]
Day_list = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
Hor_list = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
Mnt_list = ["00","05","10","15","20","25","30","35","40","45","50","55"]
for Mo in (Mon_list):
    for Da in (Day_list):
       	for Ho in (Hor_list):
           for Mn in (Mnt_list):
                urls = "wget http://nmsc.kma.go.kr/emcoms/BIMG/COMS/Y2017/M08/D24/coms_mi_le1b_ir1_a_"+Mo+Da+Ho+Mn+".png"
                temp = urls.split('/')
                filename = urls.split('/')[len(temp)-1]
                print (urls)
                print ('Downloading ' + filename + '...')


