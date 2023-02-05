import numpy as np
import matplotlib.pyplot as plt


def plot_ex1(x0, x1, N):
    dt = (x1 - x0)/(N-1)

    y = np.zeros(N)
    y[0] = np.exp(x0)
    for i in range(N-1):
        y[i+1] = y[i]*(1 - dt)

    x = np.zeros(N)
    x[0] = x0
    for i in range(N):
        x[i] = x0 + i*dt

    plt.plot(x, y, label='y1 = y0*(1 - h)')


def plot_ex2(x0, x1, N):
    dt = (x1 - x0)/(N-1)

    y = np.zeros(N)
    y[0] = np.exp(x0)
    for i in range(N-1):
        y[i+1] = y[i]/(1 + dt)

    x = np.zeros(N)
    x[0] = x0
    for i in range(N):
        x[i] = x0 + i*dt

    plt.plot(x, y, label='y1 = y0/(1 + h)')


N = 51
x0 = 0
x1 = 10
x = np.zeros(N)

dt = (x1 - x0)/(N - 1)
for i in range(N):
    x[i] = x0 + i*dt


plt.plot(x, np.exp(-x), label='$e^{-x}$')
plot_ex1(x0, x1, N)
plot_ex2(x0, x1, N)

plt.title('Comparison of different methods')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()