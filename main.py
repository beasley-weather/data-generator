#!/bin/python3


import sys

import generator
import arguments


if __name__ == '__main__':
    args = arguments.parse()
    sys.exit(generator.generate(args))
