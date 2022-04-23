from pickle import TRUE
import numpy;
import matplotlib.pyplot as plt;

x0,y0 = input("Enter the initial value of x , y (float(x0),float(y0)): ").split(',')

xn =float(input("Enter the final value of x (xn): "))

n = int(input("Enter the number of intervals required: "))

h = (xn-float(x0))/n
def calcFunction (x,y):
    return h*(y*(1+x*x))

x = numpy.linspace( float(x0) , xn, num = n+1 , endpoint=TRUE)
y = numpy.zeros(n+1)
y[0] = float(y0)

print('h = ',h)

for i in range(n):
    k1 = calcFunction(x[i] , y[i])
    k2 = calcFunction(x[i] + h/2, y[i] + k1/2)
    k3 = calcFunction(x[i] + h/2, y[i] + k2/2)
    k4 = calcFunction(x[i] + h, y[i] + k3)
    k = 1/6 * (k1 + 2*k2 + 2*k3 + k4)
    y[i+1] = y[i] + k

for i in range(n+1):
    print("%.4f"%x[i],'\t',"%.4f"%y[i])
print("\n%.4f"%y[i])
plt.figure()
plt.plot(x,y,'go-')
plt.show()
