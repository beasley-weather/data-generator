#!/bin/python3


import sys
import traceback

import arguments
import db_write
import generator


import user_input
import visualize


if __name__ == '__main__':
    args = arguments.parse()
    try:
        time, data = generator.generate(args)
    except NameError as ne:
        print(ne)
        sys.exit(1)

    if args.visualize:
        visualize.display_graph(time, data, args)
        if not(user_input.yesno('Write data?')):
            sys.exit(0)

    try:
        db_write.write(time, data, args.database, args.attribute == 'temp',
                       args.attribute == 'wind')
    except Exception as e:
        traceback.print_exc()
        sys.exit(2)

    sys.exit(0)
