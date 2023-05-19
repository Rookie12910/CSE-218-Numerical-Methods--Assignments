import numpy as np

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
            if showall is True:
                print('Step : ', i+1, ' Sub-step : ',n-temp_n)
                print('A:', '\n', A)
                print('B:', '\n', B)
            temp_n -= 1
    if showall is True:    
        print('\n','Determinant of the coefficient matrix A : ',f'{flag*np.linalg.det(A):0.4f}','\n')
    X = np.zeros((n,1))
    for i in range(n-1, -1, -1):
        substractor = 0
        for j in range(i+1, n):
            substractor += sum(A[i][j] * X[j])
        X[i] = (B[i] - substractor ) / A[i][i]
    return X


if __name__== '__main__':
    n = int(input())
    A = np.zeros((n,n))
    B = np.zeros((n,1))
    for i in range(n):
        A[i] = input().split()
    for i in range(n):
        B[i] = input().split()
    Ans = GaussianElimination(A,B)
    print('Solution :')
    for i in range (len(Ans)):
        print(f'{Ans[i][0]:0.4f}')
