import sys, os
import numpy as np

a=["N(A)","ACT(A)","Cat(A)","Multi(A)"]

ind=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        ind.append([a[i],a[j]])

np.save('ind.npy',ind)

