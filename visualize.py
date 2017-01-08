def display_graph(x, y, args):
    cycles = args.cycles
    period = args.period
    lower = args.lower
    upper = args.upper

    try:
        from matplotlib import pyplot as plt
    except:
        print('ModuleNotFoundError: No module named \'matplotlib\'')
        return

    plt.xlim(0, cycles * period)
    plt.ylim(lower - 0.1, upper + 0.1)
    plt.plot(x, y)
    plt.plot(x, y, 'b.')
    plt.show()
