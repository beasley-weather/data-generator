from matplotlib import pyplot as plt
import numpy as np


def renormalize(np_arr, lower, upper):
    return abs(upper - lower) * np_arr + lower


def square_transform(np_arr):
    new_arr = [1 if e > 0 else 0 for e in np_arr]
    return np.array(new_arr)


def duty_transform(np_arr, duty_cycle):
    new_arr = [1 if (e + duty_cycle) > 0 else 0 for e in np_arr]
    return np.array(new_arr)


def duty_high_transform(np_arr):
    new_arr = [1 if (e + 0.8) > 0 else 0 for e in np_arr]
    return np.array(new_arr)


def duty_low_transform(np_arr):
    new_arr = [0 if (e + 0.8) > 0 else 1 for e in np_arr]
    return np.array(new_arr)


def generate(args):
    model = args.model

    c = args.cycles
    p = args.period
    s = args.shift
    l = args.lower
    u = args.upper
    d = args.duty

    need_to_renormalize = l != 0 or u != 1

    x = np.linspace(0, c * p, c * p + 1)
    sin_ = np.sin(2 * np.pi / p * (x - s))

    plt.xlim(0, c * p)
    plt.ylim(l -0.1, u + 0.1)

    if model == 'square':
        y = square_transform(sin_)

    elif model == 'sin':
        y = 0.5 * sin_ + 0.5

    elif model == 'duty':
        y = duty_transform(sin_, d)

    elif model == 'duty_high':
        y = duty_high_transform(sin_)

    elif model == 'duty_low':
        y = duty_low_transform(sin_)

    else:
        print('Unknown model {}.'.format(args.model))
        return -1

    if need_to_renormalize:
        y = renormalize(y, l, u)

    plt.plot(x, y,) # '.')
    plt.show()

    return 0
