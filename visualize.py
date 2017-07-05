def display_graph(x, y, args):
    cycles = args.cycles
    period = args.period
    lower = args.lower
    upper = args.upper
    t = args.start_time

    try:
        from matplotlib import pyplot as plt
    except:
        print('ModuleNotFoundError: No module named \'matplotlib\'')
        return

    plt.xlim(t, t + cycles * period)
    plt.ylim(lower - 0.1, upper + 0.1)
    plt.plot(x, y)
    plt.plot(x, y, 'b.')
    plt.show()
