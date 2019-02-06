from msmbuilder.featurizer import DihedralFeaturizer
from msmbuilder.dataset import dataset
import numpy as np
from matplotlib import pyplot as plt
import mdtraj as md
import os,sys, glob
import msmbuilder.utils
import pickle
from msmbuilder.utils import load
from msmbuilder.cluster import KMeans
from msmbuilder.cluster import KCenters
from msmbuilder.cluster import KMedoids
from msmbuilder.cluster import MiniBatchKMeans
from msmbuilder.msm import implied_timescales
from msmbuilder.msm import ContinuousTimeMSM, MarkovStateModel
from itertools import combinations
from msmbuilder.featurizer import AtomPairsFeaturizer
from msmbuilder.decomposition import tICA
from sklearn.pipeline import Pipeline
from msmbuilder.example_datasets import fetch_met_enkephalin
from matplotlib import pyplot as plt
from sklearn.externals import joblib

#Featurization
#trajs = md.load('traj0.xtc',top='conf.gro')
#Ind = trajs.topology.select("all")
#trajs1=trajs.atom_slice(Ind)
distances=[]
#os.chdir('8662/distance')
#file=glob.glob('*npy')
#list1=sorted(file,key=lambda x: int(os.path.splitext(x.split("distance")[1])[0]))
#print list1
#os.chdir('../../')
#sys.exit()
#for i in list1:
#       b=np.load('8662/distance/%s'%i)
#a=np.arange(0,528,1)
#c=np.delete(a,(0,1,2,20,23,26,28,36,73,78,89,122,123,132,145,148,150,154,155,334,339))
#c=np.delete(a,(73))
for k in range(998):
        b=np.load('distance%d.npy'%k)
        distances.append(b)

tica_model = tICA(lag_time=50,n_components=4)
tica_fit = tica_model.fit(distances)

#output =open('tica_model.npy','wb')
#pickle.dump(tica_model,output)
#output.close()

tica_transformed = tica_model.transform(distances)

output = open('tica_model.eigenvectors.npy', 'wb')
pickle.dump(tica_model.eigenvectors_, output)
output.close()

np.save('tica.npy',tica_transformed)
