#!/usr/bin/env python
import numpy as npfile
import matplotlib.pyplot as plt
import matplotlib.colors


#open files & save data into arrays
#dataFile = open('/Users/md875/data/tutorial_data/S1998148172338_chlor_a.f999x999')
#dataFile = open('C:\share/remote_sensing\data/tutorial_data\S1998148172338_chlor_a.f999x999')
dataFile = open('/media/guitar79/F40E64170E63D0E2/remote_sensing/data/tutorial_data/S1998148172338_chlor_a.f999x999')

data1 = np.fromfile(dataFile, dtype = np.float32)
dataFile.close()

#reshape 2D data to the 2D matrixs
data1 = data1.reshape([999,999])

print 'shape of the data1 array is \n\n', data1.shape

