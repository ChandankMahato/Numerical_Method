from pickle import TRUE
import time
import numpy;
import matplotlib.pyplot as plt;


print("Enter the initial value of x,y: ")
x0,y0 = input().split()
print("Enter the final value of x: ")
xn = input()
ttl_intervals : int
print("Enter the number of intervals required: ")
ttl_intervals = input()
time.sleep(2)

h = (float(xn) -float(x0))/int(ttl_intervals)
def calcFunction (x,y):
    return h*(y*(1+x*x))

x = numpy.linspace(float(x0),float(xn),num=int(ttl_intervals)+1,endpoint=TRUE)
ystar = numpy.zeros(int(ttl_intervals)+1)
ystar[0] = float(y0)

for i in range(int(ttl_intervals)):
    ystar[i+1] = ystar[i] + 0.25*(ystar[i]*(1+x[i]*x[i]))

plt.figure()
plt.plot(x,ystar,'go-')
plt.show()