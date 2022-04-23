import numpy as np;
import matplotlib.pyplot as plt

def f(x,y):
    return y*(1+x**2)

def printTabular():
    print('n\t\t||\t\t x\t\t||\t\t y')
    print("------------------------------------------------------------------------------")
    for i in range(n+1):
        x[i]=round(x[i],roundVal)
        y[i]=round(y[i],roundVal)
        print('🙁',i+1,'\t\t||\t\t🙁',x[i],'\t\t||\t\t🙁',y[i])

x0,y0 = input("\nEnter the initial value of x , y ( x0 , y0").split(',')
xn = float(input("\nEnter the final value of x , xn = "))
n = int(input("\nEnter the number of intervals required : "))
roundVal = int(input("\nEnter the number of digits to round to : "))
h = (xn-float(x0))/n

x = np.linspace( float(x0) , xn, num = n+1 , endpoint=1)
y = np.zeros(n+1)
y[0] = float(y0)


print('\nh = ',h)

for i in range(n):
    k1 = h * f(x[i] , y[i])
    k2 = h * f(x[i] + h/2, y[i] + k1/2)
    k3 = h * f(x[i] + h/2, y[i] + k2/2)
    k4 = h * f(x[i] + h, y[i] + k3)

    y[i+1] = y[i] + 1/6 * (k1 + 2*k2 + 2*k3 + k4)

printTabular()
print('\nf(',x[n],') = ',y[n])

plt.figure()
plt.plot(x,y,'go-')
plt.show()