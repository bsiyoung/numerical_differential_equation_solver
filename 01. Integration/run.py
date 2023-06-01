import matplotlib.pyplot as plt
import numpy as np

# Integration Interval
interval = [0, 10]

# Integration Step Size
h = 1e-5

# How many multidimensional integrals
# Get up to (n_integrals)th dimension integral
n_integrals = 2


def f(x):
    return np.sin(x)


# To save memory space
# Memory usage = Total data size / save_gap
save_step = 1000


# ======================================================================

def integrate(dx, y, res_y0=0):
    res_y = [res_y0]
    for i in range(1, len(y)):
        res_y.append(res_y[-1] + (y[i] + y[i - 1]) * dx / 2)

    # float, double, longdouble
    return np.array(res_y, dtype=np.double)


# Domain of x
x_domain = np.arange(interval[0], interval[1], h)

# integrals[n] = n dimensional integral
integrals = [f(x_domain)]
for int_dim in range(1, n_integrals + 1):
    integrals.append(integrate(h, integrals[-1]))
    integrals[-2] = integrals[-2][::save_step]
    print("\r{}/{}".format(int_dim, n_integrals), end='')
x_domain = x_domain[::save_step]
integrals[-1] = integrals[-1][::save_step]

# Plot data
plt.figure(figsize=(10, 4))
plt.tight_layout()
plt.plot(x_domain, integrals[0], color=[1, 0, 0])
plt.plot(x_domain, integrals[1], color=[0, 1, 0])
plt.plot(x_domain, integrals[2], color=[0, 0, 1])
plt.show()
