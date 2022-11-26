# Importing NumPy Library
import numpy as np
import sys
import time




def sol(x):
    # Displaying solution
    print('\nRequired solution is: ')
    for i in range(n):
        print('X%d = %0.2f' %(i,x[i]), end = '\t')


def Gauss(a):
    # Making numpy array of n size and initializing 
    # to zero for storing solution vector
    x = np.zeros(n)

    # Applying Gauss Elimination
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
            
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]
    # Back Substitution
    x[n-1] = a[n-1][n]/a[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        
        x[i] = x[i]/a[i][i]
    return x


def GaussJordan(a):
    # Making numpy array of n size and initializing 
    # to zero for storing solution vector
    x = np.zeros(n)

    # Applying Gauss Jordan Elimination
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
            
        for j in range(n):
            if i != j:
                ratio = a[j][i]/a[i][i]

                for k in range(n+1):
                    a[j][k] = a[j][k] - ratio * a[i][k]

    # Obtaining Solution

    for i in range(n):
        x[i] = a[i][n]/a[i][i]
    
    return x


def gaussSeidel(a, x, b):
    #Finding length of a(3)       
    n = len(a)                   
    # for loop for 3 times as to calculate x, y , z
    for j in range(0, n):        
        # temp variable d to store b[j]
        d = b[j]                  
          
        # to calculate respective xi, yi, zi
        for i in range(0, n):     
            if(j != i):
                d-=a[j][i] * x[i]
        # updating the value of our solution        
        x[j] = d / a[j][j]
    # returning our updated solution           
    return x


def valid(old, new, epsilon):
    for i in range(len(old)):
        if abs(old[i]-new[i]) > epsilon:
            return False
    return True

def GaussSeidel(a, epsilon):
    n = a.shape[0]
    b = a[:,n:n+1].reshape(n,).tolist()
    a = a/10
    print(a)
    a = a[:,0:n].tolist()

    
    
    x_old = np.random.rand(n)
    x_new = np.zeros(n)
    while not valid(x_old, x_new, epsilon):
        for i in range(len(x_old)):
            x_old[i] = x_new[i]
        x_new = gaussSeidel(a, x_new, b)
    return x_new


# if __name__ == "__main__":
#     m = np.array([1,2,3,4])
#     print(m.shape)

#     # Reading number of unknowns
#     n = 300
#     np.random.seed(18)

#     # Making numpy array of n x n+1 size and initializing 
#     # to zero for storing augmented matrix
#     # a = np.array([  [4,1,2,4],
#     #                 [3,5,1,7],
#     #                 [1,1,3,3]])

#     a = np.random.rand(n,n+1)
#     d = np.eye(n)*3
#     d = np.append(d, np.zeros(n).reshape(n,1), axis=1)
#     a = a+d

#     # start = time.time()
#     # Gauss(a)
#     # end = time.time()
#     # print(end - start)

#     # start = time.time()
#     # GaussJordan(a)
#     # end = time.time()
#     # print(end - start)

#     start = time.time()
#     x = GaussSeidel(a, 0.001)
#     print(x)
#     end = time.time()
#     print(end - start)


#      Gauss Seidel Iteration

# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x,y,z: (17-y+2*z)/20
f2 = lambda x,y,z: (-18-3*x+z)/20
f3 = lambda x,y,z: (25-2*x+3*y)/20

# Initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1

# Reading tolerable error
e = float(input('Enter tolerable error: '))

# Implementation of Gauss Seidel Iteration
print('\nCount\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0,y0,z0)
    y1 = f2(x1,y0,z0)
    z1 = f3(x1,y1,z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);
    
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1
    
    condition = e1>e and e2>e and e3>e

print('\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n'% (x1,y1,z1))