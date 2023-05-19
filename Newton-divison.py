import numpy as np
import matplotlib.pyplot as mplt
import csv

def b0(x0,temparature,solubility_1):
    i = np.where(temparature==x0)[0][0]
    return solubility_1[i]
def b1(x1,x0,temparature,solubility_1):
    num = b0(x1,temparature,solubility_1)-b0(x0,temparature,solubility_1)
    den = x1 - x0
    return num/den
def b2(x2,x1,x0,temparature,solubility_1):
    num = b1(x2,x1,temparature,solubility_1)- b1(x1,x0,temparature,solubility_1)
    den = x2 - x0
    return num/den

def b3(x3,x2,x1,x0,temparature,solubility_1):
    num = b2(x3,x2,x1,temparature,solubility_1)- b2(x2,x1,x0,temparature,solubility_1)
    den = x3 - x0
    return num/den

def b4(x4,x3,x2,x1,x0,temparature,solubility_1):
    num = b3(x4,x3,x2,x1,temparature,solubility_1)- b3(x3,x2,x1,x0,temparature,solubility_1)
    den = x4 - x0
    return num/den

def quad_get_ans(x,x2,x1,x0,temparature,solubility_1):
    ans = b0(x0,temparature,solubility_1) + (b1(x1,x0,temparature,solubility_1)*(x-x0)) + (b2(x2,x1,x0,temparature,solubility_1)*(x-x0)*(x-x1))
    return ans

def cub_get_ans(x,x3,x2,x1,x0,temparature,solubility_1):
    ans = b0(x0,temparature,solubility_1) + (b1(x1,x0,temparature,solubility_1)*(x-x0)) + (b2(x2,x1,x0,temparature,solubility_1)*(x-x0)*(x-x1)) + (b3(x3,x2,x1,x0,temparature,solubility_1)*(x-x0)*(x-x1)*(x-x2))
    return ans

def quar_get_ans(x,x4,x3,x2,x1,x0,temparature,solubility_1):
    ans = b0(x0,temparature,solubility_1) + (b1(x1,x0,temparature,solubility_1)*(x-x0)) + (b2(x2,x1,x0,temparature,solubility_1)*(x-x0)*(x-x1)) + (b3(x3,x2,x1,x0,temparature,solubility_1)*(x-x0)*(x-x1)*(x-x2)) + (b4(x4,x3,x2,x1,x0,temparature,solubility_1)*(x-x0)*(x-x1)*(x-x2)*(x-x3))
    return ans

if __name__== '__main__':
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
    #print(quar_get_ans(x,x4,x3,x2,x1,x0,temparature,solubility_1))
    x = np.linspace(0,50,100)
    y = quar_get_ans(x,40,30,20,15,10,temparature,solubility_1)
    mplt.plot(x,y,'-b')
    mplt.xlabel("X")
    mplt.ylabel("f(x)")
    mplt.grid()
    mplt.show()
    


