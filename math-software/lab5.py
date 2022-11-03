import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return 2*x**3 - 3*x**2 + 1

def f2(x):
    return x**4 - 2*x**2 - 1

def f3(x):
    return x**3/3 + 2*x**2 + 4*x

x = np.linspace(start=-3, stop=3, num=1000)
fig, axes = plt.subplots(nrows=3, ncols=1)
axes[0].plot(x, f1(x))
axes[1].plot(x, f2(x))
axes[2].plot(x, f3(x))
fig.tight_layout()
plt.show()



# ===============
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(start=-3, stop=3, num=10)
plt.plot([0,1,2,3,4], [1,2,3,4,10], 'b-')
plt.plot([0,1,2,3,4], [10,4,3,2,1], 'r-')
plt.plot([2.5,2.5,2.5,1.5,0.5], [1,3,5,7,10], 'g-')
plt.show()
