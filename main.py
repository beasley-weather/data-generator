#!/bin/python3


import sys

import arguments
import db_write
import generator


if __name__ == '__main__':
    args = arguments.parse()
    try:
        data = generator.generate(args)
    except NameError as ne:
        print(ne)
        sys.exit(1)

    try:
        db_write.write(data, args.database, args.attribute == 'temp',
                       args.attribute == 'wind')
    except Exception as e:
        print(e)
        sys.exit(2)

    sys.exit(0)
