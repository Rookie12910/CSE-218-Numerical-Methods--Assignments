import numpy as np
import matplotlib.pyplot as mplt

def error(new,old):
    return abs((new-old)/new)*100

def bisection (xl,xu,approx_error,fun_val,max_iteration = 100):
    xm = (xl+xu)/2
    old = xm
    if fun_val(xl)* fun_val(xm)>0:
        xl = xm
    elif fun_val(xl)* fun_val(xm)<0:
        xu = xm
    xm = (xl+xu)/2
    new = xm
    iteration_count = 1
    while error(new,old)>=approx_error and iteration_count<=max_iteration:
        old = xm
        if fun_val(xl)* fun_val(xm)>0:
            xl = xm
        elif fun_val(xl)* fun_val(xm)<0:
            xu = xm
        xm = (xl+xu)/2
        new = xm
        iteration_count+=1
    return xm

def LinearModel(x,y):
    x = np.array(x)
    y = np.array(y)
    n = x.shape[0]
    sum_xy = np.sum(x*y)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xsq = np.sum(x**2)
    a1 = (n*sum_xy - (sum_x*sum_y)) / (n*sum_xsq - (sum_x**2))
    a0 = (sum_xsq*sum_y - sum_x*sum_xy) / (n*sum_xsq - (sum_x**2))
    return a0,a1

def ExpModel (x,y,byTrans = True):
    x = np.array(x)
    y = np.array(y)
    if byTrans is True:
        z = np.log(y)
        a0, a1 = LinearModel(x, z)
        B = a1
        A = np.exp(a0)
        return A, B
    else :
        def fun_val(B):            
            sum1 = np.sum(y * x * np.exp(B * x))
            sum2 = np.sum(y * np.exp(B * x))
            sum3 = np.sum(np.exp(2 * B * x))
            sum4 = np.sum(x * np.exp(2 * B * x))
            fun = (sum1 - sum2) / (sum3 * sum4)
            return fun
        B = bisection(-10, 10, 0.005, fun_val)
        A = np.sum(y*np.exp(B*x)) / np.sum(np.exp(2*B*x))
        return A, B

def PowerModel(x,y):
    z = np.log(y)
    w = np.log(x)
    a0,a1 = LinearModel(w,z)
    B = a1
    A  = np.exp(a0)
    return A,B
def GrowthModel(x,y):
    z = 1/y
    w = 1/x
    a0,a1 = LinearModel(w,z)
    A  = 1/a0
    B = a1/a0
    return A,B

def dataGraph(x,y):
    mplt.plot(x, y, 'bo',markersize = 4)
    #mplt.xlabel("X")
    #mplt.ylabel("Y")
    #mplt.grid()
    #mplt.show()

def ExpModelGraph(A,B):
    x = np.linspace(0,10,500)
    y = A*np.exp(B*x)
    mplt.plot(x, y, '-g', markerfacecolor='blue', markersize=6)
    mplt.xlabel("X")
    mplt.ylabel("Y")
    mplt.grid()
    mplt.show()

if __name__ == '__main__' :
    x = [0,1,3,5,7,9]
    y = [1.000,0.891,0.708,0.562,0.447,0.355]
    # x = [0, .01, .03, .05, .07, .09, .11, .13, .15, .17, .19, .21]
    # y = [1, 1.03, 1.06, 1.38, 2.09, 3.54, 6.41, 12.6, 21.2, 39.05, 65.32, 99.78]
    dataGraph(x,y)
    A,B = ExpModel(x,y,True)
    ExpModelGraph(A,B)
    print(A," ",B)
    TH = [0.698132,0.959931,1.134464,1.570796,1.919862]
    TR = [0.188224,0.209138,0.230052,0.250965,0.313707]
    dataGraph(TH,TR)
    a,b = LinearModel(TH,TR)
    print(a," ",b)
    Ca = [4,2.25,1.45,1.0,0.65,0.25,0.006]
    minus_ra =np.array([0.398,0.298,0.238,0.198,0.158,0.098,0.048])
    K,n = PowerModel(Ca,minus_ra)
    print(K," ",n)