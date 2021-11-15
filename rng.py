def rng(*args):
    if len(args) == 1:
        start, step, stop = 0, 1, args[0]

    elif len(args) == 2:
        start, step, stop = args[0], 1, args[1]

    elif len(args) == 3:
        start, step, stop = args[0], args[2], args[1]

        if args[2] < 0:
            while start > stop:
                yield start
                start += step
        else:
            while start < stop:
                yield start
                start += step

for i in rng(-10, 6, 1):
    print(i)
