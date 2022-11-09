import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from functools import partial

def f(x):
    return x**3-3*x-3

a = -2.2
b = 2.4

fig, ax = plt.subplots()
x = np.linspace(a, b, 1000)
y = f(x)
ax.plot(x, y)
line1, = ax.plot([], [], 'ro')

def init():
    ax.set_xlim(a-1, b+1)
    ax.set_ylim(-10, 10)
    return line1,

def update(frame, ln, x, y):
    print("frame", frame)
    x.append(frame)
    y.append(f(frame))
    ln.set_data(x, y)
    return ln,

def next_range(a, b, f):
    c = (a+b)/2
    print(a, b, c)
    print(f(a), f(b), f(c))
    if f(c)*f(b) < 0:
        return b, c
    if f(a)*f(c) < 0:
        return a, c
    else:
        return None, None

def algo(a, b, f, Err=0.001):
    c_arr = [b]
    print('f(b) = ', f(b))
    while abs(f(b)) > Err:
        a, b = next_range(a, b, f)
        if a == None:
            return c_arr
        print(b, f(b))
        c_arr.append(b)
    return c_arr

c_arr = algo(a, b, f)

print(c_arr)

ani = FuncAnimation(
    fig, partial(
        update, 
        ln=line1, x=[], y=[]),
    frames=c_arr,
    init_func=init,
    repeat_delay=1000,
    repeat=False,
    blit=True,
)

plt.show()