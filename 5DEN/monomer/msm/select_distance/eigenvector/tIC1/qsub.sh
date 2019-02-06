#!/bin/sh
#PBS -l walltime=24:00:00
#PBS -N caldis_14121
#PBS -q normal 
#PBS -l nodes=1:ppn=1
#PBS -o caldis_14121 
#PBS 

cd $PBS_O_WORKDIR

python cal_dis.py
