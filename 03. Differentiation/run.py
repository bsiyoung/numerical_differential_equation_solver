import matplotlib.pyplot as plt
import numpy as np

# Differentiation Interval
diff_interval = [0, 20]

# Differentiation Step Size
h = 1e-3

# How many derivatives
# Get up to (n_diffs)th order derivative
n_diff = 5


def f(x):
    return np.sin(x)


# To save memory space
# Memory usage = Total data size / save_gap
save_step = 100


# ======================================================================

def differentiate(dx, y):
    res_y = [(y[1] - y[0]) / dx]
    for i in range(1, len(y)-1):
        res_y.append((y[i+1] - y[i-1]) / (2 * dx))
    res_y.append((y[-1] - y[-2]) / dx)

    # float, double, longdouble
    return np.array(res_y, dtype=np.double)


# Domain of x
x_domain = np.arange(diff_interval[0], diff_interval[1], h)

# diffs[n] = n-th order derivative
diffs = [f(x_domain)]
for int_dim in range(n_diff):
    diffs.append(differentiate(h, diffs[-1]))
    diffs[-2] = diffs[-2][::save_step]
x_domain = x_domain[::save_step]
diffs[-1] = diffs[-1][::save_step]

# Plot data
plt.figure(figsize=(10, 6))
plt.tight_layout()
plt.plot(x_domain, diffs[0], color='r')
plt.plot(x_domain, diffs[1], color='g')
plt.plot(x_domain, diffs[2], color='b')
plt.show()
