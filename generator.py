import numpy as np


def renormalize(np_arr, lower, upper):
    return abs(upper - lower) * np_arr + lower


def square_transform(np_arr):
    new_arr = [1 if e > 0 else 0 for e in np_arr]
    return np.array(new_arr)


def duty_transform(period, cycles, duty_cycles):
    arr = [0 if (period * duty_cycles) <= i else 1
               for i in range(period + 1)]
    return np.tile(np.array(arr), cycles)


def generate(args):
    model = args.model

    c = args.cycles
    p = args.period
    s = args.shift
    l = args.lower
    u = args.upper
    d = args.duty
    t = args.start_time
    if (t == 0): print('Warning using default start time of 0.')

    need_to_renormalize = l != 0 or u != 1

    x = np.linspace(t, t + c * p, c * (p + 1))
    sin_ = np.sin(2 * np.pi / p * (x - s))

    if model == 'square':
        y = square_transform(sin_)

    elif model == 'sin':
        y = 0.5 * sin_ + 0.5

    elif model == 'duty':
        y = duty_transform(p, c, d)

    elif model == 'duty_high':
        y = duty_high_transform(sin_)

    elif model == 'duty_low':
        y = duty_low_transform(sin_)

    else:
        raise NameError('Unknown model {}'.format(args.model))

    if need_to_renormalize:
        y = renormalize(y, l, u)

    return x, y
