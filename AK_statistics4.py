# -*- coding: utf-8 -*-
# Auther guitar79@naver.com 

import numpy as np
import os
import pandas as pd

# data head
# ['지역', '측정소코드', '측정소명', '측정일시', 'SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM25', '주소']

#th_list = [0,5,10,15,20,25,30,35,40,45,50,55,60,65]

#base directory
drbase = '/media/guitar79/8T/RS_data/Remote_Sensing/2017RNE/airkorea/'
#read directory(input data)
drin = 'temp/'
#write directory(output data)
drout = 'output/'

f = 0

#read data files 
for i in sorted(os.listdir(drbase+drin)):
    #read csv files
    if i[-4:] == '.csv':
        #make data frame from reading csv files (like table)
        f = pd.read_csv(drbase+drin+i, encoding='euc_kr')
        #merge data frames
        f = f.append(f)
        #count number of the total data 
total_datanum = len(f)
#make observatory code index
ocode = list(set(np.array(f.ix[:,1])))
#count number of the observatory
onumber = len(ocode)
        #statistics of total data
total_mean_value = f.mean()
total_var_value = f.var()
total_std_value = f.std()
total_max_value = f.max()
total_min_value = f.min()
        #write files from statistics
with open(drbase+drout+'statistics_total.txt', 'a') as o:
    print(total_datanum,'mean',total_mean_value,'var',total_var_value,'std',total_std_value,'mas',total_max_value,'min',total_min_value, file=o)


'''
      for obs in ocode:
                fo=f.loc[f[:,1] == obs]
                #fo=f[f['측정소코드']].isin(obs)
                o_datanum = len(fo)
                if o_datanum != 0:
                    o_mean_value = fo.mean().reshape(1,11)
                    o_var_value = fo.var().reshape(1,11)
                    o_std_value = fo.std().reshape(1,11)
                    o_max_value = fo.max().reshape(1,11)
                    o_min_value = fo.min().reshape(1,11)
                    with open(drbase+drout+'statistics_'+obs+'o.txt', 'a') as o:
                        print(i, obs, o_datanum, o_mean_value, o_var_value, o_std_value, o_max_value, o_min_value, file=o)
                else:
                    with open(drbase+drout+'statistics_'+obs+'o.txt', 'a') as o:
                        print(i, obs, 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN', file=o)
'''