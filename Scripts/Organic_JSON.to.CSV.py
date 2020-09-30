import os
import shlex
import subprocess
import json
from collections import Counter
import json 
import csv
import pandas as pd
import time
import glob
all_smells=['LazyClass','ComplexClass','LongParameterList','FeatureEnvy','LongMethod','BlobClass','MessageChain','RefusedBequest','SpaghettiCode','SpeculativeGenerality']
my_map = {}


#Set the environment variable
ECLIPSE_PATH ='C:/Users/AQ42770/Desktop/eclipse/plugins'
EQUINOX = ECLIPSE_PATH+'/org.eclipse.equinox.launcher_1.3.100.v20150511-1540.jar'
MAIN='org.eclipse.core.launcher.Main'
ORGANIC='organic.Organic'
path='C:/Users/AQ42770/Desktop/NetGuard-current'


list=[]
for n in range(60,81):
    
    path1= path+"/"+str(n)
    outversion = "C:/Users/AQ42770/Desktop/NetGuard-current/"+"out"+str(n)+".json"
    commande='java -jar -XX:MaxPermSize=2560m -Xms40m -Xmx2500m "%s" %s -application %s -sf "%s" -src "%s"'
    commande= commande % (EQUINOX, MAIN, ORGANIC, outversion, path1)
    args = shlex.split(commande)
    p = subprocess.Popen(args)

    
    
    list.append(outversion)
    
print(list)


time.sleep(1200)

for elem in list:
    
    with open(elem) as f_json:
        json_data = json.load(f_json)
    for entry in json_data:
        my_map[entry["fullyQualifiedName"]] = []

        #adding all class smells 
        for class_smell in entry["smells"] :
            my_map[entry["fullyQualifiedName"]].append(class_smell)

        #adding all methods smells  
        for method in entry["methods"] :
            for method_smell in method["smells"] :
                my_map[entry["fullyQualifiedName"]].append(method_smell)


for x in range(0,74):
    output1="output"+str(x)+".csv"
    with open(output1, 'w', newline='') as f_output:
        csv_output = csv.DictWriter(f_output, fieldnames=["Class", *all_smells], extrasaction='ignore', restval='NaN')
        csv_output.writeheader()
        for elem in my_map:
            smell_counts = Counter()
            smell_counts['Class'] = elem
            for smell in my_map[elem] :
                smell_counts[smell["name"]] += 1
            csv_output.writerow(smell_counts)
time.sleep(900)

os.chdir('C:/Users/AQ42770/Desktop/BlackLight')
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
for file in all_filenames:
    df = pd.read_csv(file)
    a=df.loc[~df.Class.duplicated(keep='last')]
    a.to_csv(file, index=False, na_rep='NaN')
    m=pd.read_csv(file)
    pd.options.display.float_format = '{:,.0f}'.format
    m=m.fillna(0)
    m = m.astype({"LazyClass": int, "ComplexClass": int, "LongParameterList" : int, "FeatureEnvy" : int, "LongMethod" : int, "BlobClass" : int, "BlobClass" : int, "BlobClass" : int, "MessageChain" : int, "RefusedBequest" : int, "SpaghettiCode" : int, "SpeculativeGenerality" : int})
    m.to_csv(file, index=False, na_rep='NaN')



    


                  
    

          

    
    

    
    
