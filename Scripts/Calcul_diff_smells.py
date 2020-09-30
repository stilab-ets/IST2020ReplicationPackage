import pandas as pd 
import csv
for n in range (0,46):
    path1="C:/Users/AQ42770/Desktop/Notpad-current/mergeallsmell"+str(n)+".csv"
    resultdiffsmell="resultdiffsmell"+str(n)+".csv"
    df=pd.read_csv(path1)
    list1=[]
    for elm in df['DTWC_y']-df['DTWC_x']:
        list1.append(elm)
    print(list1)
    df['DTWC_diff'] = list1


    list2=[]
    for elm in df['DR_y']-df['DR_x']:
        list2.append(elm)
    print(list2)
    df['DR_diff'] = list2

    list3=[]
    for elm in df['DW_y']-df['DW_x']:
        list3.append(elm)
    print(list3)
    df['DW_diff'] = list3

    list4=[]
    for elm in df['IDFP_y']-df['IDFP_x']:
        list4.append(elm)
    print(list4)
    df['IDFP_diff'] = list4

    list5=[]
    for elm in df['IDS_y']-df['IDS_x']:
        list5.append(elm)
    print(list5)
    df['IDS_diff'] = list5

    list6=[]
    for elm in df['ISQLQ_y']-df['ISQLQ_x']:
        list6.append(elm)
    print(list6)
    df['ISQLQ_diff'] = list6

    list7=[]
    for elm in df['IGS_y']-df['IGS_x']:
        list7.append(elm)
    print(list7)
    df['IGS_diff'] = list7

    list8=[]
    for elm in df['LIC_y']-df['LIC_x']:
        list8.append(elm)
    print(list8)
    df['LIC_diff'] = list8

    list9=[]
    for elm in df['LT_y']-df['LT_x']:
        list9.append(elm)
    print(list9)
    df['LT_diff'] = list9

    list10=[]
    for elm in df['MIM_y']-df['MIM_x']:
        list10.append(elm)
    print(list10)
    df['MIM_diff'] = list10

    list11=[]
    for elm in df['NLMR_y']-df['NLMR_x']:
        list11.append(elm)
    print(list11)
    df['NLMR_diff'] = list11

    list12=[]
    for elm in df['PD_y']-df['PD_x']:
        list12.append(elm)
    print(list12)
    df['PD_diff'] = list12

    list13=[]
    for elm in df['RAM_y']-df['RAM_x']:
        list13.append(elm)
    print(list13)
    df['RAM_diff'] = list13

    list14=[]
    for elm in df['SL_y']-df['SL_x']:
        list14.append(elm)
    print(list14)
    df['SL_diff'] = list14

    list15=[]
    for elm in df['UC_y']-df['UC_x']:
        list15.append(elm)
    print(list15)
    df['UC_diff'] = list15

    
    list16=[]
    for elm in df['LazyClass_y']-df['LazyClass_x']:
        list16.append(elm)
    print(list16)
    df['LazyClass_diff'] = list16

    list17=[]
    for elm in df['ComplexClass_y']-df['ComplexClass_x']:
        list17.append(elm)
    print(list17)
    df['ComplexClass_diff'] = list17

    list18=[]
    for elm in df['LongParameterList_y']-df['LongParameterList_x']:
        list18.append(elm)
    print(list18)
    df['LongParameterList_diff'] = list18

    list19=[]
    for elm in df['FeatureEnvy_y']-df['FeatureEnvy_x']:
        list19.append(elm)
    print(list19)
    df['FeatureEnvy_diff'] = list19

    list20=[]
    for elm in df['LongMethod_y']-df['LongMethod_x']:
        list20.append(elm)
    print(list20)
    df['LongMethod_diff'] = list20

    list21=[]
    for elm in df['BlobClass_y']-df['BlobClass_x']:
        list21.append(elm)
    print(list21)
    df['BlobClass_diff'] = list21

    list22=[]
    for elm in df['MessageChain_y']-df['MessageChain_x']:
        list22.append(elm)
    print(list22)
    df['MessageChain_diff'] = list22

    list23=[]
    for elm in df['RefusedBequest_y']-df['RefusedBequest_x']:
        list23.append(elm)
    print(list23)
    df['RefusedBequest_diff'] = list23


    list24=[]
    for elm in df['SpaghettiCode_y']-df['SpaghettiCode_x']:
        list24.append(elm)
    print(list8)
    df['SpaghettiCode_diff'] = list24

    list25=[]
    for elm in df['SpeculativeGenerality_y']-df['SpeculativeGenerality_x']:
        list25.append(elm)
    print(list25)
    df['SpeculativeGenerality_diff'] = list25

   

   

    df.to_csv(resultdiffsmell,index=False)



