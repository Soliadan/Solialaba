from math import sin
def func(x):
    total = 0
    k = 1
    d = 0.001
    while True:
        f = (((-1)**k * x)/(k*(k+1))) * sin(2 * k +1 )
        if (abs(f) < d):
            break
        total += f
        k += 1
    return total
    
for i in range (-10, 11, 5):
    x = i / 10
    y = func(x)
    print(f"x={x:.2f}, f(x)={y:.3f}")