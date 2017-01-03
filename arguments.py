import argparse


def parse():
    parser = argparse.ArgumentParser(description='Test data generator.')
    parser.add_argument('attribute',
                        help='Data attribute to generate (wind, temp).')
    parser.add_argument('model',
                        help='Data model (square, sin, duty_high, duty_low).')
    parser.add_argument('-c', '--cycles', type=int, default=1,
                        help='Number of cycles.')
    parser.add_argument('-p', '--period', type=int, default=24,
                        help='Period for model (hours).')
    parser.add_argument('-s', '--shift', type=int, default=0,
                        help='Time shift for model (hours).')
    parser.add_argument('-u', '--upper', type=int, default=1,
                        help='Upper limit on model.')
    parser.add_argument('-l', '--lower', type=int, default=0,
                        help='Lower limit on model.')
    parser.add_argument('-d', '--duty', type=float, default=0.5,
                        help='Duty cycle for duty model.')
    return parser.parse_args()
