
import operator
from functools import reduce
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
data = pd.read_csv("combinefinal.csv")
count_row = data.shape[0]
a= data['NLMR_y'].values.tolist()
b=data['Extract And Move Method'].values.tolist()
Class = data ['Class'].values.tolist()
#print(a)
#print(b)
class_a=[]
class_b=[]
for i in range(0,len(a)):
        if a [i] >=1:
            class_a.append([Class [i]])
#print(class_a)
h=len(class_a)
for i in range(0,len(b)):
        if b[i] >=1:
            class_b.append([Class [i]])
#print(class_b)

liste1=[]
liste=[]
for a in range (0,len(class_a)):
    for b in range (0,len(class_b)):
        Intersection=list(set(class_a[a])& set(class_b[b]))
        Union=list(set().union(class_a[a],class_b[b]))
        #print(Intersection)
        liste.append(Intersection)
        





list2 = [x for x in liste if x != []]
#print(list2)
l=len(list2)




support=l/count_row
print(support)

confidence=l/h
print(confidence)

for a in range (0,len(class_a)):
        Intersection=list(set(class_a[a]))
        
        liste.append(Intersection)
list2 = [x for x in liste if x != []]
#print(list2)
dedup = [list2[i] for i in range(len(list2)) if i == 0 or list2[i] != list2[i-1]]
#print(dedup)
l1=len(dedup)
suppa=l1/count_row
print(suppa)


for a in range (0,len(class_a)):
        Intersection=list(set(class_b[a]))
      
        liste.append(Intersection)
list = [x for x in liste if x != []]
#print(list2)
dedup = [list2[i] for i in range(len(list2)) if i == 0 or list2[i] != list2[i-1]]
#print(dedup)
l2=len(dedup)
suppb=l2/count_row
print(suppb)
        
        
