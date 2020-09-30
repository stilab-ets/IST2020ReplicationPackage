import pandas as pd
import time
for n in range (0,11):
    result=""
    path1="C:/Users/AQ42770/Documents/Android-ColorPicker/outdoctor"+str(n)+".csv"
    path2="C:/Users/AQ42770/Documents/Android-ColorPicker/output"+str(n)+".csv"
    a = pd.read_csv(path1)
    b = pd.read_csv(path2)

    merged = a.merge(b, on='Class')
    result="result"+str(n)+".csv"
    merged.to_csv(result, index=False)


time.sleep(60)
for n in range (0,11):
    result="result"+str(n)+".csv"
    df = pd.read_csv(result)
    k=df.loc[~df.Class.duplicated(keep='last')]
    k.to_csv(result, index=False, na_rep='NaN')



