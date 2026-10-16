for i in range(5, 0, -1):
    print(' '*(5-i) + ' '.join(str(x) for x in range(1, i+1)))
