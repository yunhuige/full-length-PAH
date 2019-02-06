import sys, os
import numpy as np
from matplotlib import pyplot as plt
t1=np.load('../../tica2.npy')[0:150000:1]
t2=np.load('../../tica2.npy')[150000:300000:1]
t3=np.load('../../tica2.npy')[300000:450000:1]
t4=np.load('../../tica2.npy')[450000:600000:1]
t5=np.load('../../tica2.npy')[600000::1]
#print t1[0], t1[1]
color=['blue','green','gold','red','black','magenta']
#l=['TRP6-PHE1','TRP6-PRO10']
b=[]
c=[]
avg=[]
for j in range(3):
        d1=np.load('%d.npy'%j)[0:150000:1]*10.0
        d2=np.load('%d.npy'%j)[150000:300000:1]*10.0
        d3=np.load('%d.npy'%j)[300000:450000:1]*10.0
        d4=np.load('%d.npy'%j)[450000:600000:1]*10.0
        d5=np.load('%d.npy'%j)[600000::1]*10.0
#y=[]
#err=[]

# the bins of the histogram (tIC1 coords)
        x=np.arange(-35.,5.0,0.05)

# calculate a Gaussian kernel weighted average for each bin position
        sigma = 0.2
        avg_d_vs_t1 = np.zeros( x.shape )
        for i in range(len(x)):
            weights = (1./(2.0*np.pi*sigma**2)**0.5)*np.exp( -(t1 - x[i])**2/(2.0*sigma**2) ) 
            avg_d_vs_t1[i] = np.dot(weights,d1)/weights.sum()

        avg_d_vs_t2 = np.zeros( x.shape )
        for i in range(len(x)):
            weights = (1./(2.0*np.pi*sigma**2)**0.5)*np.exp( -(t2 - x[i])**2/(2.0*sigma**2) )
            avg_d_vs_t2[i] = np.dot(weights,d2)/weights.sum()

        avg_d_vs_t3 = np.zeros( x.shape )
        for i in range(len(x)):
            weights = (1./(2.0*np.pi*sigma**2)**0.5)*np.exp( -(t3 - x[i])**2/(2.0*sigma**2) )
            avg_d_vs_t3[i] = np.dot(weights,d3)/weights.sum()

        avg_d_vs_t4 = np.zeros( x.shape )
        for i in range(len(x)):
            weights = (1./(2.0*np.pi*sigma**2)**0.5)*np.exp( -(t4 - x[i])**2/(2.0*sigma**2) )
            avg_d_vs_t4[i] = np.dot(weights,d4)/weights.sum()

        avg_d_vs_t5 = np.zeros( x.shape )
        for i in range(len(x)):
            weights = (1./(2.0*np.pi*sigma**2)**0.5)*np.exp( -(t5 - x[i])**2/(2.0*sigma**2) )
            avg_d_vs_t5[i] = np.dot(weights,d5)/weights.sum()



#if (0):
#  counts,bins=np.histogram(t1,x)
#  for i in range(0,len(x)-1):
#	a=[]
#	for j in range(len(t1)):
#		if t1[j]< x[i+1] and t1[j]> x[i]:
#			a.append(d[j])
#	y.append(sum(a))
#print len(counts)
#print len(y)
#print counts
#print y
#print y
#print len(y)
#	err.append(np.std(a))
#	if sum(a)==0 or counts[i]==0:
#		y.append(0.0)
#	else:
#		y.append(sum(a)/float(counts[i]))	

        y=[]
        err=[]
        for j in range(len(avg_d_vs_t1)):
	        y.append(np.mean([avg_d_vs_t1[j],avg_d_vs_t2[j],avg_d_vs_t3[j],avg_d_vs_t4[j],avg_d_vs_t5[j]]))
	        err.append(np.std([avg_d_vs_t1[j],avg_d_vs_t2[j],avg_d_vs_t3[j],avg_d_vs_t4[j],avg_d_vs_t5[j]]))
        b.append(np.array(y)+np.array(err))
        c.append(np.array(y)-np.array(err))
        avg.append(y)

#b=np.array(y)+np.array(err)
#c=np.array(y)-np.array(err)
#print b
#print c
#sys.exit()
#bincenters=(bins[0:-1]+bins[1:])/2.0
plt.figure(figsize=(1.6,3.3))
#plt.plot(x,y,color='magenta')
for k in range(len(avg)):
    plt.plot(y,avg[k],color='magenta')
#plt.errorbar(bincenters,y,yerr=err)
#plt.fillbetweenx(x,c,b)
    plt.fill_betweenx(x,c[k],b[k],color='magenta',alpha=0.2)
#plt.fill_between(x,c,b,color='magenta',alpha=0.2)
#plt.plot(x,avg_d_vs_t1)
#plt.plot(x,avg_d_vs_t2)
#plt.plot(x,avg_d_vs_t3)
#plt.plot(x,avg_d_vs_t4)
#plt.plot(x,avg_d_vs_t5)
plt.ylim(min(x),max(x))
plt.xticks(fontsize=6.5)
plt.yticks(fontsize=6.5)
#plt.xlim(min(bincenters),max(bincenters))
#plt.yticks([])
#plt.ylabel('Distance (nm)',fontsize=7)
#plt.xlabel('tIC2', fontsize=7)
#plt.savefig('1PHE-4LEU.pdf')
plt.savefig('tICA2.pdf')
plt.show()


