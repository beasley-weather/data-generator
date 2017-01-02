#!/bin/python3

import argparse
from matplotlib import pyplot as plt
import numpy as np
import sys


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


def main(args):
    model = args.model

    c = args.cycles
    p = args.period
    l = args.lower
    u = args.upper
    d = args.duty

    need_to_renormalize = l != 0 or u != 1

    x = np.linspace(0, c * p, c * p + 1)
    sin_ = np.sin(2 * np.pi / p * x)

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
        sys.exit(1)

    if need_to_renormalize:
        y = renormalize(y, l, u)

    plt.plot(x, y,) # '.')
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test data generator.')
    parser.add_argument('attribute',
                        help='Data attribute to generate (wind, temp).')
    parser.add_argument('model',
                        help='Data model (square, sin, duty_high, duty_low).')
    parser.add_argument('-c', '--cycles', type=int, default=1,
                        help='Number of cycles.')
    parser.add_argument('-p', '--period', type=int, default=24,
                        help='Period for model (hours).')
    parser.add_argument('-u', '--upper', type=int, default=1,
                        help='Upper limit on model.')
    parser.add_argument('-l', '--lower', type=int, default=0,
                        help='Lower limit on model.')
    parser.add_argument('-d', '--duty', type=float, default=0.5,
                        help='Duty cycle for duty model.')
    args = parser.parse_args()

    main(args)
