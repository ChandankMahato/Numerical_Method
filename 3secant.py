MAX_ITER = 6
#The function is x^3 - x -1 = 0,

def func(x):
    return (x*x*x - x - 1)

def secantMethod(a,b):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return -1
    c = a
    for i in range(MAX_ITER):
        c = (a*func(b) - b * func(a)) / (func(b) - func(a))
        if(func(c) == 0):
            break
        else:
            a=b
            b=c
        print("The value of root is:","%.4f" %c)
a = 1
b = 2
secantMethod(a, b)