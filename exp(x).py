import numpy as np
import matplotlib.pyplot as plt


def plot_ex(x0, x1, N):
    dt = (x1 - x0)/(N-1)

    y = np.zeros(N)
    y[0] = np.exp(x0)
    for i in range(N-1):
        y[i+1] = y[i]*(1 - dt)

    x = np.zeros(N)
    x[0] = x0
    for i in range(N):
        x[i] = x0 + i*dt

    plt.plot(x, y, label=f'n = {n}')


N = 101
x0 = 0
x1 = 10
x = np.zeros(N)

dt = (x1 - x0)/(N - 1)
for i in range(N):
    x[i] = x0 + i*dt

for i in range(5):
    n = (i + 1)*10 + 1
    plot_ex(x0, x1, n)

plt.plot(x, np.exp(-x), label='$e^{-x}$')

plt.title('$e^{-x}$ with different n')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()





