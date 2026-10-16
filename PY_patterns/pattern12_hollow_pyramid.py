for i in range(1, 6):
    print(' ' * (5 - i), end='')
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == 5:
            print('*', end='')
        else:
            print(' ', end='')
    print()
