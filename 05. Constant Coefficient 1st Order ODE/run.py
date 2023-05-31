import matplotlib.pyplot as plt
import numpy as np

# 1st ODE Form
# (Dy)(x) + c0 * y(x) = r(x)

interval = [0, 30]
dx = 1e-5
save_gap = 100

# Initial value (at x=0)
# Up to one value can be None
init_val = {
    'D0': 1,  # y(0)
    'D1': None  # y'(0)
}

# ODE Params
c0 = 1


def r(x):
    return np.sin(x)


# ==============================================================

# Calculate initial value explicitly
if init_val['D0'] is None:
    if c0 == 0:
        init_val['D0'] = 0
    else:
        init_val['D0'] = (r(0) - init_val['D1']) / c0
elif init_val['D1'] is None:
    init_val['D1'] = r(0) - c0 * init_val['D0']

x_domain = np.arange(interval[0], interval[1], dx)

res_y = [init_val['D0']]
for curr_x in x_domain[1:]:
    dy = (r(curr_x) - c0 * res_y[-1]) / (1 + c0 * dx) * dx
    res_y.append(res_y[-1] + dy)
x_domain = x_domain[::save_gap]
res_y = res_y[::save_gap]

plt.figure(figsize=(10, 4))
plt.tight_layout()
plt.plot(x_domain, res_y, color='r')
plt.show()
