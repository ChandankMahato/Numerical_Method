x=float(input("x0 = "))
xn=float(input("xn = "))
y=float(input("y0 = "))
n=int(input("n = "))
h=(xn-x)/n

f = lambda x,y: y*(1+x**2)

while(x != xn):
    k1 = h * f(x,y)
    k2 = h * f(x + h/2 ,y + k1/2)
    k3 = h * f(x + h/2, y + k2/2)
    k4 = h * f(x + h ,y + k3)

    y = y + 1/6 * (k1+2*k2+2*k3+k4)
    x=x+h

print("Ans = ",y)
