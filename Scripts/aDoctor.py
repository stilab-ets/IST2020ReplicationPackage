
import json
from collections import Counter
import json 
import csv
import pandas as pd
import glob
import time
import os
import shlex
import subprocess

os.chdir('C:/Users/AQ42770/Desktop/aDoctor')
path='C:/Users/AQ42770/Desktop/Apg-current'
for n in range(0,68):
    
    path1= path+"/"+str(n)
    outversion = "C:/Users/AQ42770/Desktop/Ap-current/"+"doctor"+str(n)+".csv"
    cmd='java -cp aDoctor-1.0.jar it.unisa.aDoctor.process.RunAndroidSmellDetection %s %s "111111111111111"'
    cmd = cmd % (path1,outversion)
    args = shlex.split(cmd)
    p = subprocess.Popen(args)

