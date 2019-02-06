import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm


#tica_transformed = np.load('tica_2a.npy')
#tica_transformed = np.concatenate(tica_transformed) 
a=np.load('tica1.npy')

#a=np.concatenate(a)
print len(a)
b=np.load('tica2.npy')
#b=np.concatenate(b)

#plt.figure(figsize=(3.3,3))
plt.figure()
plt.hist2d(a,b,bins=300,norm=LogNorm())
#plt.hist2d(tica_transformed[:,0],tica_transformed[:,1],bins=300,norm=LogNorm())
plt.xlim(-13,2)
plt.ylim(-1.2,7)
#plt.xticks([])
#plt.yticks([])
plt.xlabel("tIC1")
plt.ylabel("tIC2")
#plt.title("tICA Heatmap total")
plt.savefig("tica1v2.pdf")
plt.show()
#plt.savefig("tica1v2_plot.pdf")

