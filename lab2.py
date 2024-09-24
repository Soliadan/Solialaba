import math 

h = 0.02
a = 0.5
b = 0.8

def func(x):
    if x < 0.6:
        return math.exp(x - math.sin(x))
    elif 0.6 <= x < 0.7:
        return math.tan(abs(math.log(x)))
    elif x >= 0.7:
        return math.atan(x ** 7)
    

x = a
while x <= b:
    y = func(x)
    if y is not None:
        print(f"x = {x:.2f}, f(x) = {y:.3f}")
    x += h
