import numpy as np
import matplotlib.pyplot as mplt

def fun_val(x):
    return (x**3)-(0.18*(x**2))+(4.75*(10**-4))
def der_fun_val(x):
    return (3*(x**2))-(0.36*x)
def error(new,old):
    return abs((new-old)/new)*100
def bisection (xl,xu,approx_error,max_iteration):
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
        print("Error in Bisection Method",iteration_count,"th iteration:",error(new,old),"%")
        old = xm
        if fun_val(xl)* fun_val(xm)>0:
            xl = xm
        elif fun_val(xl)* fun_val(xm)<0:
            xu = xm
        xm = (xl+xu)/2
        new = xm
        iteration_count+=1
    print("Error in Bisection Method",iteration_count,"th iteration:",error(new,old),"%")
    return xm
def NewtonRaphson(x1,approx_error,max_iteration):
    x2 = x1 - (fun_val(x1)/der_fun_val(x1))
    iteration_count = 1
    while error(x2,x1)>=approx_error and iteration_count<=max_iteration:
        print("Error in Newton-Raphson Method ",iteration_count,"th iteration:",error(x2,x1),"%")
        x1 = x2;
        x2 = x1 - (fun_val(x1)/der_fun_val(x1))
        iteration_count+=1
    print("Error in Newton-Raphson Method ",iteration_count,"th iteration:",error(x2,x1),"%")
    return x2;
        

if __name__== '__main__':
    approx_error = 0.5
    max_iteration = input("Maximum number of iteration : ")
    print()
    max_iteration = int(max_iteration)
    value = bisection(0.0,0.12,approx_error,max_iteration) #Guess value obtained from graph
    print("Root obtained by Bisection Method : ",value)
    print()
    value = NewtonRaphson(0.06,approx_error,max_iteration) #Guess value obtained from graph
    print("Root obtained by Newton-Raphson Method : ",value)
    x = np.linspace(0,0.15,100)
    y = fun_val(x)
    mplt.plot(x,y,'-b')
    mplt.xlabel("X")
    mplt.ylabel("f(x)")
    mplt.grid()
    mplt.show()
    
    

