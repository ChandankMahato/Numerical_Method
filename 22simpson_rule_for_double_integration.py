import numpy as np

# Class qn soln for simpson rule for double integration:
def f(x,y):
    return x**2 + np.exp(y)

a = 2
b = 3
c = 0
d = 2
n = 4

h = np.around((b - a) / n,4)
k = np.around((d - c) / n,4)

func_table=[[0 for row in range(0,n+2)] for col in range(0,n+2)] # one exra row and coumn for table row and column heading
print("The functional value table is:-"+'\n')
for i in range(n+2):
         for j in range(n+2):
            if(i == 0 and j == 0):
                func_table[i][j] = "f(x,y)"
            elif(i == 0):
                func_table[i][j] = func_table[i][j-1] + k if func_table[i][j-1] != "f(x,y)" else c
            elif(j==0):
                func_table[i][j] =  func_table[i-1][j] + h if func_table[i-1][j] != "f(x,y)" else a
            else:
                func_table[i][j] = np.around(f(func_table[i][0],func_table[0][j]),4)


# Display the functional value table
for i in range(n+2):
         for j in range(n+2):
             print(func_table[i][j],end=' '* (8 - len(str(func_table[i][j]))))
         print("\n")

def label(k):
    if(k == 1):
        return 4
    elif(k == 4):
        return 2
    elif(k == 2):
        return 4
    else:
        return 1

coeff_table=[[0 for row in range(0,n+2)] for col in range(0,n+2)]
print("The coefficient table for simpson's rule is:")
for i in range(n+2):
         for j in range(n+2):
            if(i == 0 and j == 0):
                coeff_table[i][j] = "*"
            elif(i == 0):
                if(j == n+1):
                    coeff_table[i][j] = 1
                else:
                    coeff_table[i][j] = label(coeff_table[i][j-1])
            elif(j == 0):
                if(i == n+1):
                    coeff_table[i][j] = 1
                else:
                    coeff_table[i][j] = label(coeff_table[i-1][j])
            else:
                coeff_table[i][j] = coeff_table[i][0] * coeff_table[0][j]

# Display the coefficient tavle
for i in range(n+2):
         for j in range(n+2):
             print(coeff_table[i][j],end=' '* (8 - len(str(coeff_table[i][j]))))
         print("\n")

# sum of multiples of functional value and coefficient table
sum = 0
for i in range(1,n+2):
         for j in range(1,n+2):
             sum += func_table[i][j] * coeff_table[i][j]

print("The value of double integration by Simpson Rule:",np.around((h*k*sum)/9,4))