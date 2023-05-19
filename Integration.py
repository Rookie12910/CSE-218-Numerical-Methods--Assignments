import numpy as np
import matplotlib.pyplot as mplt

def fun_val(x):
    Cme = 5 * 10**-4
    num = (6.73*x + 6.725*10**-8 + Cme*7.26*10**-4)
    den = (3.62*x*10**-12 + Cme*3.908*x*10**-8)
    return -(num/den)
def error(new,old):
    return (abs(new-old)/new)*100
def trapezoid_result(a,b,n):
    h = (b-a)/n
    fa = fun_val(a)
    fb = fun_val(b)
    mid_term = 0
    for i in range(1,n):
        mid_term = mid_term + fun_val(a+i*h)
    return h/2*(fa + 2*mid_term + fb)
def Simpson_result(a,b,n):
    h = (b-a)/n
    fa = fun_val(a)
    fb = fun_val(b)
    odd_terms = fun_val(a+h)
    even_terms = 0
    for i in range(1,int(n/2)):
        odd_terms = odd_terms + fun_val(a+(2*i+1)*h)
        even_terms = even_terms + fun_val(a+(2*i)*h)
    return h/3*(fa + 4*odd_terms + 2*even_terms + fb)


if __name__ == '__main__':
    x0 = 1.22 * 10 ** -4
    x = [1.22*10**-4,1.20*10**-4,1.0*10**-4,0.8*10**-4,0.6*10**-4,0.4*10**-4,0.2*10**-4]
    x = np.array(x)
    y = Simpson_result(x0, x,10)
    mplt.plot(x, y, '-g',marker = 'o',markerfacecolor = 'blue',markersize = 6)
    mplt.xlabel("Oxygen concentration")
    mplt.ylabel("Time")
    mplt.grid()
    mplt.show()

    n = int(input("Enter the numbers of segments : "))
    a = (75 / 100) * x0
    b = (25 / 100) * x0

    print("Using trapezoid rule :")
    for i in range(1,n+1):
        if i==1:
            ans1 = trapezoid_result(a, b, i)
            print("Result for ", i, " segments : ", ans1)
        elif i > 1:
            ans2 = trapezoid_result(a, b, i)
            print("Result for ",i," segments : ",ans2)
            print("Relative error :",error(ans2,ans1),"%")
            ans1 = ans2

    print("\nUsing Simpson's 1/3 rule :")
    for i in range(1,n+1):
        if i==1:
            ans1 = Simpson_result(a, b, 2*i)
            print("Result for ", 2*i, " segments : ", ans1)
        elif i > 1:
            ans2 = Simpson_result(a, b, 2*i)
            print("Result for ",2*i," segments : ",ans2)
            print("Relative error :",error(ans2,ans1),"%")
            ans1 = ans2
