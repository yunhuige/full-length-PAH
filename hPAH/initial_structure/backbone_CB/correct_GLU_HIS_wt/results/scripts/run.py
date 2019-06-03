import os,sys,glob
import itertools

#nsystems=1
nsystems=8
mini_runs=6 #1 minimization. the rest of runs are restrainting 4helicals
all_runs=15
free_runs=30

#print ("run section 1")
#for _ in itertools.repeat(None,mini_runs):
#    os.system('python runme_mini.py ../solv_ions.gro ../new.top')
#print ("run section 2")

#for _ in itertools.repeat(None,all_runs):
#    os.system('python runme_all.py ../solv_ions.gro ../new.top')

print ("run section 3")
for _ in itertools.repeat(None,free_runs):
    os.system('python runme_free.py ../solv_ions.gro ../new.top')
