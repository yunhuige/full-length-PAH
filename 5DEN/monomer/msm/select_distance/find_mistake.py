import numpy as np
a=np.load('tica.npy')
for i in range(len(a)):
	for j in range(len(a[i])):
		if a[i][j][1]<-10.0:
			print 'traj', i, 'frame', j
			break
