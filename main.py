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

    db_write.write(data, args.database, args.attribute == 'temp',
                   args.attribute == 'wind')

    sys.exit(0)
