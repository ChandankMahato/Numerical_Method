decimal_places = 5

# manually provide the functions and their partial derivatives wrt x and y:
def func_f(x, y):
  '''Returns f at (x, y)'''
  val = x**2 - y**2 - 4
  return round(val, decimal_places)

def func_g(x, y):
  '''Returns g at (x, y)'''
  val = x**2 + y**2 - 16
  return round(val, decimal_places)

def df_by_dx(x, y):
  '''Returns ∂f/∂x at (x, y)'''
  val = 2*x
  return round(val, decimal_places)
  
def df_by_dy(x, y):
  '''Returns ∂f/∂y at (x, y)'''
  val = -2*y
  return round(val, decimal_places)

def dg_by_dx(x, y):
  '''Returns ∂g/∂x at (x, y)'''
  val = 2*x
  return round(val, decimal_places)

def dg_by_dy(x, y):
  '''Returns ∂g/∂y at (x, y)'''
  val = 2*y
  return round(val, decimal_places)

def print_row(x, y, f, g, a, b, c, d, D, D1, D2, h, k):
  print(f"""{x:<12.5f} {y:<12.5f} {f:<12.5f} {g:<12.5f} {a:<12.5f} {b:<12.5f} \
{c:<12.5f} {d:<12.5f} {D:<12.5f} {D1:<12.5f} {D2:<12.5f} {h:<12.5f} {k:<12.5f}""")

def evaluate(x_old, y_old):
  #table header
  print(f"""{'x':{12}} {'y':{12}} {'f':{12}} {'g':{12}} {'a (∂f/∂x)':{12}} \
{'b (∂f/∂y)':{12}} {'c (∂g/∂x)':{12}} {'d (∂g/∂y)':{12}} {'D (ad - bc)':{12}} \
{'D1 (-fd+gb)':{12}} {'D2 (-ga+fc)':{12}} {'h (D1/D)':{12}} {'k (D2/D)':{12}}""")

  while (True):
    f = func_f(x_old, y_old)
    g = func_g(x_old, y_old)
    
    a = df_by_dx(x_old, y_old) #∂f/∂x
    b = df_by_dy(x_old, y_old) #∂f/∂y
    c = dg_by_dx(x_old, y_old) #∂g/∂x
    d = dg_by_dy(x_old, y_old) #∂g/∂y

    D = round(a * d - b * c, decimal_places)
    if (D == 0):
      print("D can not be zero. Please change your initial guess.")
      break

    D1 = round(-f * d + g * b, decimal_places)
    D2 = round(-g * a + f * c, decimal_places)

    h = round(D1 / D, decimal_places)
    k = round(D2 / D, decimal_places)
    
    print_row(x_old, y_old, f, g, a, b, c, d, D, D1, D2, h, k)
    
    # check if the root is found.
    if (h == 0 and k == 0):
      print(f"\nRoot is x = {x_old:.5f}, y = {y_old:.5f}")
      break
    
    x_old = round(x_old + h, decimal_places)
    y_old = round(y_old + k, decimal_places)
evaluate(2, 2) # provide the intial guesses for x and y wisely