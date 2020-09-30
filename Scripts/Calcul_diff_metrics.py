import pandas as pd 
import csv
for n in range (0,46):
    path1="C:/Users/AQ42770/Desktop/Notpad-current/merge_metrics/mergemetrics"+str(n)+".csv"
    calculMetrics="calculMetrics"+str(n)+".csv"


    df=pd.read_csv(path1)
    list=[]
    for elm in df['cbo_y']-df['cbo_x']:
        list.append(elm)
    print(list)
    df['cbo_diff'] = list

    list1=[]
    for elm in df['wmc_y']-df['wmc_x']:
        list1.append(elm)
    print(list1)
    df['wmc_diff'] = list1

    list2=[]
    for elm in df['dit_y']-df['dit_x']:
        list2.append(elm)
    print(list2)
    df['dit_diff'] = list2

    list3=[]
    for elm in df['rfc_y']-df['rfc_x']:
        list3.append(elm)
    print(list3)
    df['rfc_diff'] = list3

    list4=[]
    for elm in df['lcom_y']-df['lcom_x']:
        list4.append(elm)
    print(list4)
    df['lcom_diff'] = list4

    list5=[]
    for elm in df['totalMethods_y']-df['totalMethods_x']:
        list5.append(elm)
    print(list5)
    df['totalMethods_diff'] = list5

    list6=[]
    for elm in df['staticMethods_y']-df['staticMethods_x']:
        list6.append(elm)
    print(list6)
    df['staticMethods_diff'] = list6

    list7=[]
    for elm in df['staticMethods_y']-df['staticMethods_x']:
        list7.append(elm)
    print(list7)
    df['staticMethods_diff'] = list7


    list8=[]
    for elm in df['publicMethods_y']-df['publicMethods_x']:
        list8.append(elm)
    print(list8)
    df['publicMethods_diff'] = list8

    list9=[]
    for elm in df['privateMethods_y']-df['privateMethods_x']:
        list9.append(elm)
    print(list9)
    df['privateMethods_diff'] = list9

    list10=[]
    for elm in df['protectedMethods_y']-df['protectedMethods_x']:
        list10.append(elm)
    print(list10)
    df['protectedMethods_diff'] = list10


    list11=[]
    for elm in df['defaultMethods_y']-df['defaultMethods_x']:
        list11.append(elm)
    print(list11)
    df['defaultMethods_diff'] = list11

    list12=[]
    for elm in df['abstractMethods_y']-df['abstractMethods_x']:
        list12.append(elm)
    print(list12)
    df['abstractMethods_diff'] = list12

    list13=[]
    for elm in df['finalMethods_y']-df['finalMethods_x']:
        list13.append(elm)
    print(list13)
    df['finalMethods_diff'] = list13

    list14=[]
    for elm in df['synchronizedMethods_y']-df['synchronizedMethods_x']:
        list14.append(elm)
    print(list14)
    df['synchronizedMethods_diff'] = list14

    list15=[]
    for elm in df['totalFields_y']-df['totalFields_x']:
        list15.append(elm)
    print(list15)
    df['totalFields_diff'] = list15

    list16=[]
    for elm in df['staticFields_y']-df['staticFields_x']:
        list16.append(elm)
    print(list16)
    df['staticFields_diff'] = list16

    list17=[]
    for elm in df['publicFields_y']-df['publicFields_x']:
        list17.append(elm)
    print(list17)
    df['publicFields_diff'] = list17

    list18=[]
    for elm in df['privateFields_y']-df['privateFields_x']:
        list18.append(elm)
    print(list18)
    df['privateFields_diff'] = list18

    list19=[]
    for elm in df['protectedFields_y']-df['protectedFields_x']:
        list19.append(elm)
    print(list19)
    df['protectedFields_diff'] = list19

    list20=[]
    for elm in df['defaultFields_y']-df['defaultFields_x']:
        list20.append(elm)
    print(list20)
    df['defaultFields_diff'] = list20

    list21=[]
    for elm in df['finalFields_y']-df['finalFields_x']:
        list21.append(elm)
    print(list21)
    df['finalFields_diff'] = list21

    list22=[]
    for elm in df['synchronizedFields_y']-df['synchronizedFields_x']:
        list22.append(elm)
    print(list22)
    df['synchronizedFields_diff'] = list22

    list23=[]
    for elm in df['nosi_y']-df['nosi_x']:
        list23.append(elm)
    print(list23)
    df['nosi_diff'] = list23

    list24=[]
    for elm in df['loc_y']-df['loc_x']:
        list24.append(elm)
    print(list24)
    df['loc_diff'] = list24

    list25=[]
    for elm in df['returnQty_y']-df['returnQty_x']:
        list25.append(elm)
    print(list25)
    df['returnQty_diff'] = list25

    list26=[]
    for elm in df['loopQty_y']-df['loopQty_x']:
        list26.append(elm)
    print(list26)
    df['loopQty_diff'] = list26

    list27=[]
    for elm in df['comparisonsQty_y']-df['comparisonsQty_x']:
        list27.append(elm)
    print(list27)
    df['lcomparisonsQty_diff'] = list27

    list28=[]
    for elm in df['tryCatchQty_y']-df['tryCatchQty_x']:
        list28.append(elm)
    print(list28)
    df['tryCatchQty_diff'] = list28

    list29=[]
    for elm in df['parenthesizedExpsQty_y']-df['parenthesizedExpsQty_x']:
        list29.append(elm)
    print(list29)
    df['parenthesizedExpsQty_diff'] = list29

    list30=[]
    for elm in df['stringLiteralsQty_y']-df['stringLiteralsQty_x']:
        list30.append(elm)
    print(list30)
    df['stringLiteralsQty_diff'] = list30


    list31=[]
    for elm in df['numbersQty_y']-df['numbersQty_x']:
        list31.append(elm)
    print(list31)
    df['numbersQty_diff'] = list31

    list32=[]
    for elm in df['assignmentsQty_x']-df['assignmentsQty_y']:
        list32.append(elm)
    print(list32)
    df['assignmentsQty_diff'] = list32

    list33=[]
    for elm in df['mathOperationsQty_y']-df['mathOperationsQty_x']:
        list33.append(elm)
    print(list33)
    df['mathOperationsQty_diff'] = list33

    list34=[]
    for elm in df['variablesQty_y']-df['variablesQty_x']:
        list34.append(elm)
    print(list34)
    df['variablesQty_diff'] = list34

    list35=[]
    for elm in df['maxNestedBlocks_y']-df['maxNestedBlocks_x']:
        list35.append(elm)
    print(list35)
    df['maxNestedBlocks_diff'] = list35

    list36=[]
    for elm in df['anonymousClassesQty_y']-df['anonymousClassesQty_x']:
        list36.append(elm)
    print(list36)
    df['anonymousClassesQty_diff'] = list36

    list37=[]
    for elm in df['subClassesQty_y']-df['subClassesQty_x']:
        list37.append(elm)
    print(list37)
    df['subClassesQty_diff'] = list37

    list38=[]
    for elm in df['lambdasQty_y']-df['lambdasQty_x']:
        list38.append(elm)
    print(list38)
    df['lambdasQty_diff'] = list38

    list39=[]
    for elm in df['uniqueWordsQty_y']-df['lambdasQty_x']:
       list39.append(elm)
    print(list39)
    df['lambdasQty_diff'] = list39

    """list40=[]
    for elm in df['Unnamed..40_y']-df['Unnamed..40_x']:
        list40.append(elm)
    print(list40)
    df['Unnamed..40_diff'] = list40"""

    df.to_csv(calculMetrics,index=False)



