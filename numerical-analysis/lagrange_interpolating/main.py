import numpy as np
import matplotlib.pyplot as plt

def lagrange(data_x, data_y, x):
    y_ans = 0
    for i in range(data_x.size):
        p = data_y[i]
        for j in range(data_x.size):
            if i != j:
                p *= ((x - data_x[j]) / (data_x[i] - data_x[j]))
        y_ans += p
    return y_ans


if __name__ == "__main__":
    x = np.array([-3,-2,-1,0])
    y = np.array([1/10,1/5,1/2,1])

    gx = np.linspace(-200,300,1000)
    gy = [lagrange(x, y, p) for p in gx]
    # plot the function
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    # red dashes, blue squares and green triangles
    plt.plot(x, y, 'g^')
    plt.plot(gx,gy, 'r')
    plt.show()