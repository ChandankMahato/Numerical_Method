from cmath import sqrt


MAX_ITER = 7

#The function is x^3 - x - 1 = 0

def func1(x):
    return ((x+1) ** (1/3))

def iteration1(x):
    c = x
    for i in range(MAX_ITER):
        c = func1(c)
        print("The value of root is: ", "%.4f" %c)
        if(func1(c) == 0):
            break

def func2(x):
    return (((x+1)/x) ** (1/2))

def iteration2(x):
    d = x
    for i in range(MAX_ITER):
        d = func2(d)
        print("The value of root is: ", "%.4f" %d)
        if(func2(d) == 0):
            break

a = 1
iteration1(a)
print("#########################################")
iteration2(a)
