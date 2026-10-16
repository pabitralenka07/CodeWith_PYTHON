n = 7

for i in range(n):
    for j in range(n):
            if (i == 0 and j == n // 2) or \
            (i == 1 and (j == n // 2 - 1 or j == n // 2 + 1)) or \
            (i == 2 and (j == 0 or j == 1 or j == 2 or
                            j == n - 3 or j == n - 2 or j == n - 1)) or \
            (i == 3) or \
            (i == 4 and (j == 0 or j == 1 or j == 2 or
                            j == n - 3 or j == n - 2 or j == n - 1)) or \
            (i == 5 and (j == n // 2 - 1 or j == n // 2 + 1)) or \
            (i == 6 and j == n // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()
    