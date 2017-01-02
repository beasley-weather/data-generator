import argparse
from matplotlib import pyplot as plt
import numpy as np
import sys


def square_transform(np_arr):
    return [1 if e > 0 else 0 for e in np_arr]


def duty_high_transform(np_arr):
    return [1 if (e + 0.8) > 0 else 0 for e in np_arr]


def duty_low_transform(np_arr):
    return [0 if (e + 0.8) > 0 else 1 for e in np_arr]


def main(args):
    p = args.period

    x = np.linspace(0, p, p)
    sin_ = np.sin(2 * np.pi / p * x)

    plt.xlim(0, p)
    plt.ylim(-.1, 1.1)

    if args.model == 'square':
        y = square_transform(sin_)
        plt.plot(x, y, '.')
        plt.show()

    elif args.model == 'sin':
        y = 0.5 * sin_ + 0.5
        plt.plot(x, y, '.')
        plt.show()

    elif args.model == 'duty_high':
        y = duty_high_transform(sin_)
        plt.plot(x, y, '.')
        plt.show()

    elif args.model == 'duty_low':
        y = duty_low_transform(sin_)
        plt.plot(x, y, '.')
        plt.show()

    else:
        print("Unknown model")
        sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test data generator.')
    parser.add_argument('attribute',
                        help='Data attribute to generate (wind, temp).')
    parser.add_argument('model',
                        help='Data model (square, sin, duty_high, duty_low).')
    parser.add_argument('-p', '--period', type=int, default=24,
                        help='Period for model (hours).')
    args = parser.parse_args()

    main(args)
