import csv
import pandas as pd

for i in range(0,81):
   out="output"+str(i)+".csv"
   file="file"+str(i)+".csv"
    
   df=pd.read_csv(out, sep=',')
   df1 = df[['RefactoringType','RefactoringDetail']]
   df1['Detail']=df.RefactoringDetail.str.extract(r'[C|c]lass\s*([^ ]*)')
   del df1['RefactoringDetail']
   my_map={}
   for i in range(df1.shape[0]):
       my_map[df1['Detail'][i]] = []
       my_map[df1['Detail'][i]].append(df1['RefactoringType'][i])
       print(my_map)
   all_refactorings=['Extract Superclass','Extract Method','Inline Method','Rename Method','Move Method','Rename Package','Move Attribute','Pull Up Method','Pull Up Attribute','Push Down Method','Push Down Attribute','Move Class','Rename Class','Move And Rename Class','Extract And Move Method','Move Source Folder','Change Package','Extract Variable','Rename Attribute','Move and Rename Attribute','Replace Variable with Attribute','Replace Attribute ','Merge Variable','Merge Parameter','Merge Attribute','split Variable','split Parameter','Split Attribute','Extract Interface']
   newdf = pd.DataFrame(columns= ['Class'] + all_refactorings )
   for class_name in my_map :
       new_row = {ref:0 for ref in all_refactorings} 
       new_row['Class'] = class_name
       for ref_type in my_map[class_name] :
           new_row[ref_type] += 1 
           newdf=newdf.append(new_row, ignore_index=True)

   newdf.to_csv(file, index=False, na_rep='NaN')
