# -*- coding: utf-8 -*-
"""
@author: guitar79@naver.com, yyyyy@snu.ac.kr
#http://nmsc.kma.go.kr/emcoms/BIMG/COMS/Y2017/M08/D24/coms_mi_le1b_ir1_a_201708240545.png
"""
import urllib.request
for year in range(2017,2018):
	for Mo in range(1,13):
		for Da in range(1,32):
			for Ho in range(24):
				for Mn in range(0,60,15): # looks like the interval is 15min. often omitted.
					url = "http://nmsc.kma.go.kr/emcoms/BIMG/COMS/Y%d/M08/D24/coms_mi_le1b_ir1_a_%d%02d%02d%02d%02d.png" \
					% (year, Mo, Da, year, Mo, Da, Ho, Mn)
					filename = url.split('/')[-1]
					try:
						urllib.request.urlretrieve(url, 'Downloads/%s' % filename)
						print ('Trying %s' % url)
						print ('Downloaded %s' % filename)
						
					except urllib.error.HTTPError: # image file doens't exists
						print ('Passed %s' % filename)