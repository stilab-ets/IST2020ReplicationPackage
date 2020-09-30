import csv
import pandas as pd
df=pd.read_csv('all_refactorings.csv', sep=';')
df1 = df[['CommitId','RefactoringType','RefactoringDetail']]
df1['Detail']=df.RefactoringDetail.str.extract(r'[C|c]lass\s*([^ ]*)')
del df1['RefactoringDetail']
a=df1.loc[~df.CommitId.duplicated(keep='last')]
print(a)
list=[]
for elm in a['CommitId']:
    list.append(elm)
dicts = {key: d for key, d in df.groupby('CommitId')}

lenght=len(list)

for i in range(lenght):
    output1="output"+str(i)+".csv"
    a=dicts[list[i]]
    m=pd.DataFrame.from_dict(a) 
    m.to_csv(output1, index=False, na_rep='NaN')
