import matplotlib.pyplot as plt
import numpy as np

# 1st ODE Form
# (D^2y)(x) + c1 * (Dy)(x) + c0 * y(x) = r(x)

interval = [0, 15]
dx = 1e-6
save_gap = 100

# Initial value (at x=0)
# Up to one value can be None
# init_val[n] = (D^n y)(0)
init_val = [1.0, 0.0]

# ODE Params
c = [500, 1]


def r(x):
    return 0


# ==============================================================

x_domain = np.arange(interval[0], interval[1], dx)

res_y = [[init_val[0]], [init_val[1]]]
for curr_x in x_domain[1:]:
    dy = (r(curr_x) * dx + res_y[1][-1] - c[0] * res_y[0][-1] * dx) / (1 + c[0] * (dx ** 2) + c[1] * dx) * dx
    res_y[0].append(res_y[0][-1] + dy)
    res_y[1].append(dy / dx)
x_domain = x_domain[::save_gap]
res_y[0] = res_y[0][::save_gap]

plt.figure(figsize=(10, 4))
plt.tight_layout()
plt.plot(x_domain, res_y[0], color='r')
plt.show()
