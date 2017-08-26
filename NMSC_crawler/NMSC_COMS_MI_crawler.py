# -*- coding: utf-8 -*-
"""
@author: guitar79@naver.com, yyyyy@snu.ac.kr
#http://nmsc.kma.go.kr/emcoms/BIMG/COMS/Y2017/M08/D24/coms_mi_le1b_ir1_a_201708240545.png # east asia
#http://nmsc.kma.go.kr/emcoms/BIMG/COMS/Y2017/M08/D26/coms_mi_le1b_ir1_cf_201708260215.png # fulldisk asia
"""
#chl = [vis, ir1, ir2, swir, wv]
chl = "ir1"
#area = [cf, cn, a, k, lk]
area = "a"
import urllib.request
from pathlib import Path
for year in range(2017,2018):
	for Mo in range(1,13):
		for Da in range(1,32):
			for Ho in range(24):
				for Mn in range(0,60,5): # looks like the interval is 5min. often omitted.
					url = "http://nmsc.kma.go.kr/emcoms/BIMG/COMS/Y%d/M%02d/D%02d/coms_mi_le1b_%d_%d_%d%02d%02d%02d%02d.png" \
					% (year, Mo, Da, chl, area, year, Mo, Da, Ho, Mn)
					filename = url.split('/')[-1]
					my_file = Path('Downloads/%s' % filename)
					if my_file.is_file(): # image file already exists in my folder
					    print ('File exists')
					else:
					    try:
					        print ('Trying %s' % url)
					        urllib.request.urlretrieve(url, 'Downloads/%s' % filename)
					        print ('Downloaded %s' % filename)
					    except  FileNotFoundError: # image file doesn't exists in the server
					        print ('file already exist %s' % filename)
