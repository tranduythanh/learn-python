import numpy as np
import matplotlib.pyplot as plt

# Bài 1 ===========
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



# Bài 2 ===============
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(start=-3, stop=3, num=10)
plt.plot([0,1,2,3,4], [1,2,3,4,10], 'b-')
plt.plot([0,1,2,3,4], [10,4,3,2,1], 'r-')
plt.plot([2.5,2.5,2.5,1.5,0.5], [1,3,5,7,10], 'g-')
plt.show()


# Bài 3 ===============
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(start=-3, stop=3, num=10)
plt.plot([1,2,3,4,5], [1,2,3,4,10], 'go', label='Chaugnar')
plt.plot([1,2,3,4,5], [2,3,4,5,11], 'b*', label='Butterfly')
plt.plot([1,2,3,4,5], [4,5,7,2,20], 'y*', label='Sinestrea') 
plt.xlabel("x")
plt.ylabel("y")
plt.title("Just a funny graph, ahihi")
plt.legend(loc="best")
plt.show()

# Bài 4 ===============
import numpy as np
import matplotlib.pyplot as plt

divisions = ['Div-A', 'Div-B', 'Div-C', 'Div-D', 'Div-E']
division_avg_marks = [70, 82, 73, 65, 68]

plt.bar(divisions, division_avg_marks, color='green')
plt.xlabel("Divisions")
plt.ylabel("Division Marks")
plt.title("Just a funny graph, ahihi")
plt.show()


# Bài 5 ===============
import numpy as np
import matplotlib.pyplot as plt

divisions = ['Div-A', 'Div-B', 'Div-C', 'Div-D', 'Div-E']
division_avg_marks = [70, 82, 73, 65, 68]
variance = [5,8,7,6,4]

plt.barh(divisions, division_avg_marks, xerr = variance, color='green')
plt.xlabel("Divisions")
plt.ylabel("Division Marks")
plt.title("Just a funny graph, ahihi")
plt.show()

# Bài 6 ===============
import numpy as np
import matplotlib.pyplot as plt

divisions = ['Div-A', 'Div-B', 'Div-C', 'Div-D', 'Div-E']
division_avg_marks = [70, 82, 73, 65, 68]
boys_avg_marks = [68, 67, 77, 61, 70]

index=np.arange(5)
width = 0.3

plt.bar(index, division_avg_marks, width=width, color='green', label='Divisions')
plt.bar(index+width, boys_avg_marks, width=width,  color='blue', label='Boys')
plt.xlabel("Divisions")
plt.ylabel("Division Marks")
plt.title("Just a funny graph, ahihi")
plt.legend(loc='best')
plt.xticks(index+width/2, divisions)
plt.show()


# Bài 7 ===============
import numpy as np
import matplotlib.pyplot as plt

divisions = ['Div-A', 'Div-B', 'Div-C', 'Div-D', 'Div-E']
boys_avg_marks = [68, 67, 77, 61, 70]
girls_avg_marks = [72, 97, 69, 69, 66]

index=np.arange(5)
width = 0.3

plt.bar(index, boys_avg_marks, width=width, color='blue', label='Divisions')
plt.bar(index, girls_avg_marks, width=width,  color='red', label='Boys', bottom=boys_avg_marks)
plt.xlabel("Divisions")
plt.ylabel("Division Marks")
plt.title("Just a funny graph, ahihi")
plt.legend(loc='best')
plt.xticks(index, divisions)
plt.show()


# Bài 8a ===============
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

heights = np.array([167, 170, 149, 165, 155, 180, 166, 146,
                    159, 185, 145, 168, 172, 181, 169])
weights = np.array([86, 74, 66, 78, 68, 79, 90, 73, 
                    70, 88, 66, 84, 67, 84, 77])
plt.xlim(140, 200)
plt.ylim(60, 100)
plt.scatter(heights, weights)
plt.xlabel("Heights")
plt.ylabel("Weights")
plt.title("Just a funny graph, ahihi")
plt.show()

# Bài 8b ===============
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

heights = np.array([167, 170, 149, 165, 155, 180, 166, 146,
                    159, 185, 145, 168, 172, 181, 169])
weights = np.array([86, 74, 66, 78, 68, 79, 90, 73, 
                    70, 88, 66, 84, 67, 84, 77])
plt.xlim(140, 200)
plt.ylim(60, 100)

ax = plt.axes(projection='3d')
ax.scatter3D(heights, weights)
ax.set_xlabel("Heights")
ax.set_ylabel("Weights")
plt.title("Just a funny graph, ahihi")
plt.show()

# Bài 8c ===============
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

heights = np.array([167, 170, 149, 165, 155, 180, 166, 146,
                    159, 185, 145, 168, 172, 181, 169])
weights = np.array([86, 74, 66, 78, 68, 79, 90, 73, 
                    70, 88, 66, 84, 67, 84, 77])
plt.xlim(140, 200)
plt.ylim(60, 100)

ax = plt.axes(projection='3d')
ax.plot3D(heights, weights)
ax.set_xlabel("Heights")
ax.set_ylabel("Weights")
plt.title("Just a funny graph, ahihi")
plt.show()