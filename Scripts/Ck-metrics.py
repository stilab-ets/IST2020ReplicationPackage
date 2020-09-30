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
import shutil

os.chdir('C:/ck-master/target')
path='C:/Users/AQ42770/Desktop/Notpad-current/45'

    
cmd='java -jar ck-0.3.2-SNAPSHOT-jar-with-dependencies.jar "%s"'
cmd = cmd % (path)
args = shlex.split(cmd)
p = subprocess.Popen(args)
os.rename("class.csv","class45.csv")
    
    
   
    
