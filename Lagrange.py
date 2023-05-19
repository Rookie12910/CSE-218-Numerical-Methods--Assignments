import numpy as np
import matplotlib.pyplot as mplt
import csv

def fx(x,x_arr,fx_arr):
    i = np.where(x_arr==x)[0][0]
    return fx_arr[i]

def L_val(n,lv,x,cx_arr):
    value = 1
    list = []
    for i in range (0,n+1):
        if(i!=lv):
            list.append(cx_arr[i])
    for i in range(0,n):
        value = value * ((x-list[i])/(cx_arr[lv]-list[i]))
    return value

def third_ord (x,x_arr,cx_arr,fx_arr):
    ans = (L_val(3,0,x,cx_arr)*fx(cx_arr[0],x_arr,fx_arr)) + (L_val(3,1,x,cx_arr)*fx(cx_arr[1],x_arr,fx_arr)) + (L_val(3,2,x,cx_arr)*fx(cx_arr[2],x_arr,fx_arr)) + (L_val(3,3,x,cx_arr)*fx(cx_arr[3],x_arr,fx_arr))
    return ans


if __name__== '__main__':
    """
    list1 = []
    list2 = []
    list3 = []
    
    with open('dissolveO2.csv') as file:       
        reader = csv.DictReader(file) #for regular file, use csv.reader
        for row in reader:            
            list1.append(row['temparature'])
            list2.append(row['solubility_1'])
            list3.append(row['solubility_2'])
    for  i in range (0,len(list1)):
        list1[i] = float(list1[i])
        list2[i] = float(list2[i])
        list3[i] = float(list3[i])       
    temparature = np.array(list1)
    solubility_1 = np.array(list2)
    solubility_2 = np.array(list3)
    """
    list1 = [0,10,15,20,22.5,30]
    list2 = [0,227.04,362.78,517.35,602.97,901.67]
    list3 = [10,15,20,22.5]
    for  i in range (0,len(list1)):
        list1[i] = float(list1[i])
        list2[i] = float(list2[i])
        #list3[i] = float(list3[i])
    x = np.array(list1)
    y = np.array(list2)
    cx = np.array(list3)
    ans = third_ord(16,x,cx,y)
    print(ans)
    """
    x = np.linspace(0,50,100)
    y = quar_get_ans(x,40,30,20,15,10,temparature,solubility_1)
    mplt.plot(x,y,'-b')
    mplt.xlabel("X")
    mplt.ylabel("f(x)")
    mplt.grid()
    mplt.show()
    """
