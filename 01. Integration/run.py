import matplotlib.pyplot as plt
import numpy as np

int_interval = [0, 20]
dx = 1e-3

# How many multidimensional integrals
# Get up to (n_integrals)th dimension integral
n_integrals = 5

# To save memory space
# Memory usage = Total data size / save_gap
save_gap = 100


def f(x):
    return np.sin(x)


# ======================================================================

def integrate(x, y, res_y0=0):
    res_y = [res_y0]
    for i in range(1, len(y)):
        h = x[i] - x[i-1]
        res_y.append(res_y[-1] + (y[i] + y[i-1]) * h / 2)

    # float, double, longdouble
    return np.array(res_y, dtype=np.double)


# Domain of x
x_domain = np.arange(int_interval[0], int_interval[1], dx)

# integrals[n] = n dimensional integral
integrals = [f(x_domain)]
for int_dim in range(n_integrals):
    integrals.append(integrate(x_domain, integrals[-1]))
    integrals[-2] = integrals[-2][::save_gap]
x_domain = x_domain[::save_gap]
integrals[-1] = integrals[-1][::save_gap]

# Plot data
plt.figure(figsize=(10, 6))
plt.tight_layout()
plt.plot(x_domain, integrals[0], color='r')
plt.plot(x_domain, integrals[1], color='g')
plt.plot(x_domain, integrals[2], color='b')
plt.show()
