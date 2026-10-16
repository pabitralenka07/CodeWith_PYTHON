import math
for i in range(1, 6):
    for j in range(1, 6):
        if math.dist([i,j],[3,3]) <= 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()
