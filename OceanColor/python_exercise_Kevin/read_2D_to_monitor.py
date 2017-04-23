#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

#fname='C:\Users\ByungHyunKim\Desktop/dtutorial_data\S1998148172338_chlor_a.f999x999'
#fname = 'C:\share/remote_sensing\data/tutorial_data\S1998148172338_chlor_a.f999x999'
fname = '/media/guitar79/F40E64170E63D0E2/remote_sensing/data/tutorial_data/S1998148172338_chlor_a.f999x999'
f=open(fname)
d1=np.fromfile(f,dtype=np.float32)
f.close()

d1=d1.reshape([999,999])

print 'shape of d1 array',d1.shape

mycmap= plt.get_cmap('spectral')
mycmap.set_bad('k')

plt.figure(1)
plt.imshow(d1,cmap=mycmap,vmin=0.01,vmax=20.0,norm=matplotlib.colors.LogNorm())
plt.colorbar()
plt.show()
