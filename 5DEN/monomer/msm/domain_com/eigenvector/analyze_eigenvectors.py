import sys, os
import numpy as np
from matplotlib import pyplot as plt
a=np.load('tica_model.eigenvectors.npy')

# find 10 largest eigenvectors
#print abs(a[:,1]).argsort()[-10:]
b=abs(a[:,0]).argsort()[-50:]
#print b
#np.save('10_eigenvector.npy', list(reversed(b)))
#sys.exit()
# find original atom pair indices
c=np.load('ind.npy')
for i in range(len(b)):
    print c[list(reversed(b))[i]], a[list(reversed(b))[i]][0]
sys.exit()
#print len(c)
#ind=[]
for j in list(reversed(b)):
#	print j
#	if j < 1394:
		ind.append(c[j])
#	else:
#		ind.append(c[j+1])
#np.save('10_eigenvectors.npy',ind)
#sys.exit()
# find atom pairs
filename='new.pdb'

with open(filename) as f:
        lines=f.readlines()
line=''.join(lines)
fields = line.strip().split('\n')
#print fields
field=[]
for k in range((len(fields))):
        field.append(fields[k].strip().split())
d=[]
e=[]
for l in range(len(ind)):
	for m in range(len(field)):
		if ind[l][0] == int(field[m][1])-1:
			d.append(int(m))
		if ind[l][1] == int(field[m][1])-1:
			e.append(int(m)) 
for n in range(len(d)):
	print field[d[n]][4]+field[d[n]][3],":", field[d[n]][2], "--",field[e[n]][4]+field[e[n]][3],":", field[e[n]][2], "values:", str(a[:,1][list(reversed(b))[n]])







