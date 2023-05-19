import numpy as np
import matplotlib.pyplot as mplt

def GaussianElimination (A,B,pivot = True,showall = True):
    flag = 1
    n = len(A[0])
    for i in range(n-1):
        if pivot is True:
            for j in range(i,n):
                for k in range(j,n):
                    if  abs(A[j][i]) < abs(A[k][i]):
                        A[[j,k],:] = A[[k,j],:]
                        B[[j,k],:] = B[[k,j],:]
                        flag *= -1
        pivot_A = A[i]
        pivot_B = B[i]
        temp_n = n - 1
        while((temp_n-i)>0):
            multiplier = A[temp_n][i]/pivot_A[i]
            A[temp_n] = A[temp_n] - (pivot_A*multiplier)
            B[temp_n] = B[temp_n] - (pivot_B*multiplier)
            temp_n -= 1
    X = np.zeros((n,1))
    for i in range(n-1, -1, -1):
        substractor = 0
        for j in range(i+1, n):
            substractor += sum(A[i][j] * X[j])
        X[i] = (B[i] - substractor ) / A[i][i]
    return X

def PolyModel(x,y,d):
    x = np.float64(x)
    y = np.array(y)
    n = float(x.shape[0])
    T = np.zeros(2*d+1)
    TA = np.zeros(d+1)
    for i in range(1,(2*d+1)):
        T[i] = np.sum(x**i)
    for i in range(0,d+1):
        TA[i] = np.sum(x**i * y)
    X = np.array([[n,T[1],T[2]],[T[1],T[2],T[3]],[T[2],T[3],T[4]]])
    Y = np.array([[TA[0]],[TA[1]],[TA[2]]])
    Ans = GaussianElimination(X, Y)
    return Ans

def dataGraph(x,y):
    mplt.plot(x, y, 'bo',markersize = 4)
    # mplt.xlabel("X")
    # mplt.ylabel("Y")
    # mplt.grid()
    # mplt.show()
def PolyModelGraph(ans,x):
    x = np.linspace(-340,100,500)
    y = ans[0] + ans[1]*x +ans[2]*x**2
    mplt.plot(x, y, '-g')
    mplt.xlabel("X")
    mplt.ylabel("Y")
    mplt.grid()
    mplt.show()


if __name__== '__main__':
   T = [80,40,-40,-120,-200,-280,-340]
   Alp = np.array([6.47,6.24,5.72,5.09,4.30,3.33,2.45])*10**-6
   d = input("Enter the degree of the polynomial : ")
   d = int(d)

   #T = [0, .01, .03, .05, .07, .09, .11, .13, .15, .17, .19, .21]
   #Alp= [1, 1.03, 1.06, 1.38, 2.09, 3.54, 6.41, 12.6, 21.2, 39.05, 65.32, 99.78]
   dataGraph(T,Alp)
   Ans = PolyModel(T,Alp,d)
   PolyModelGraph(Ans,T)
   for i in range (len(Ans)):
        print(Ans[i][0]," ")
