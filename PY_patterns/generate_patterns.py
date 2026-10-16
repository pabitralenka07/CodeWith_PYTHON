patterns = {
    "pattern1_right_angle_triangle.py": """for i in range(1, 6):
    print('*' * i)
""",

    "pattern2_inverted_right_angle_triangle.py": """for i in range(5, 0, -1):
    print('*' * i)
""",

    "pattern3_pyramid.py": """for i in range(1, 6):
    print(' ' * (5 - i) + '*' * (2 * i - 1))
""",

    "pattern4_inverted_pyramid.py": """for i in range(5, 0, -1):
    print(' ' * (5 - i) + '*' * (2 * i - 1))
""",

    "pattern5_diamond.py": """for i in range(1, 6):
    print(' ' * (5 - i) + '*' * (2 * i - 1))
for i in range(4, 0, -1):
    print(' ' * (5 - i) + '*' * (2 * i - 1))
""",

    "pattern6_hollow_square.py": """for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print('*', end='')
        else:
            print(' ', end='')
    print()
""",

    "pattern7_full_square.py": """for i in range(5):
    print('*' * 5)
""",

    "pattern8_number_triangle.py": """for i in range(1, 6):
    print(' '.join(str(x) for x in range(1, i + 1)))
""",

    "pattern9_inverted_number_triangle.py": """for i in range(5, 0, -1):
    print(' '.join(str(x) for x in range(1, i + 1)))
""",

    "pattern10_floyd_triangle.py": """num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()
""",

    "pattern11_hollow_triangle.py": """for i in range(1, 6):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == 5:
            print('*', end='')
        else:
            print(' ', end='')
    print()
""",

    "pattern12_hollow_pyramid.py": """for i in range(1, 6):
    print(' ' * (5 - i), end='')
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == 5:
            print('*', end='')
        else:
            print(' ', end='')
    print()
""",

    "pattern13_hollow_diamond.py": """for i in range(1, 6):
    print(' ' * (5 - i), end='')
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range(4, 0, -1):
    print(' ' * (5 - i), end='')
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
""",

    "pattern14_hollow_diamond_numbers.py": """for i in range(1, 6):
    print(' ' * (5 - i), end='')
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print(i, end='')
        else:
            print(' ', end='')
    print()
""",

    "pattern15_butterfly.py": """for i in range(1, 6):
    print('*' * i + ' ' * (2*(5-i)) + '*' * i)
for i in range(5, 0, -1):
    print('*' * i + ' ' * (2*(5-i)) + '*' * i)
""",

    "pattern16_hollow_number_pyramid.py": """for i in range(1, 6):
    print(' ' * (5 - i), end='')
    for j in range(1, 2*i):
        if j == 1 or j == 2*i-1:
            print(i, end='')
        else:
            print(' ', end='')
    print()
""",

    "pattern17_full_star_pyramid.py": """for i in range(1, 6):
    print(' ' * (5 - i) + '*' * (2*i - 1))
""",

    "pattern18_inverted_full_star_pyramid.py": """for i in range(5, 0, -1):
    print(' ' * (5 - i) + '*' * (2*i - 1))
""",

    "pattern19_left_aligned_triangle.py": """for i in range(1, 6):
    print('*' * i)
""",

    "pattern20_right_aligned_triangle.py": """for i in range(1, 6):
    print(' ' * (5 - i) + '*' * i)
""",

    "pattern21_pascals_triangle.py": """import math
n = 5
for i in range(n):
    print(' '*(n-i), end='')
    for j in range(i+1):
        print(math.comb(i, j), end=' ')
    print()
""",

    "pattern22_zigzag.py": """for i in range(1, 6):
    if i % 2 == 0:
        print(' '*(i-1) + '*')
    else:
        print('*'*i)
""",

    "pattern23_hourglass.py": """for i in range(5, 0, -1):
    print(' '*(5-i) + '*'*(2*i-1))
for i in range(2, 6):
    print(' '*(5-i) + '*'*(2*i-1))
""",

    "pattern24_diamond_numbers.py": """for i in range(1, 6):
    print(' '*(5-i) + str(i)*(2*i-1))
for i in range(4, 0, -1):
    print(' '*(5-i) + str(i)*(2*i-1))
""",

    "pattern25_hollow_rhombus.py": """for i in range(5):
    print(' '*i, end='')
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print('*', end='')
        else:
            print(' ', end='')
    print()
""",

    "pattern26_numeric_pyramid.py": """for i in range(1, 6):
    print(' '*(5-i) + ' '.join(str(x) for x in range(1, i+1)))
""",

    "pattern27_hollow_diamond_numbers.py": """for i in range(1, 6):
    print(' '*(5-i), end='')
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print(i, end='')
        else:
            print(' ', end='')
    print()
""",

    "pattern28_reverse_number_pyramid.py": """for i in range(5, 0, -1):
    print(' '*(5-i) + ' '.join(str(x) for x in range(1, i+1)))
""",

    "pattern29_diamond_star.py": """for i in range(1, 6):
    print(' '*(5-i) + '*'*(2*i-1))
for i in range(4, 0, -1):
    print(' '*(5-i) + '*'*(2*i-1))
""",

    "pattern30_full_number_pyramid.py": """for i in range(1, 6):
    print(' '*(5-i) + ''.join(str(x) for x in range(1, i+1)))
""",

    "pattern31_checkerboard.py": """for i in range(5):
    for j in range(5):
        if (i+j)%2==0:
            print('*', end='')
        else:
            print(' ', end='')
    print()
""",

    "pattern32_hollow_circle.py": """import math
for i in range(1, 6):
    for j in range(1, 6):
        if math.dist([i,j],[3,3]) <= 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()
""",

    "pattern33_triangle_numbers.py": """for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end='')
    print()
""",

    "pattern34_rhombus_numbers.py": """for i in range(1, 6):
    print(' '*(5-i) + ''.join(str(x) for x in range(1,i+1)))
for i in range(4, 0, -1):
    print(' '*(5-i) + ''.join(str(x) for x in range(1,i+1)))
""",

    "pattern35_decreasing_numbers.py": """for i in range(5, 0, -1):
    print(' '.join(str(x) for x in range(1, i+1)))
""",

    "pattern36_hollow_inverted_pyramid.py": """for i in range(5, 0, -1):
    for j in range(1, 2*i):
        if j==1 or j==2*i-1 or i==5:
            print('*', end='')
        else:
            print(' ', end='')
    print()
""",

    "pattern37_cross.py": """for i in range(5):
    for j in range(5):
        if i==j or i+j==4:
            print('*', end='')
        else:
            print(' ', end='')
    print()
""",

    "pattern38_number_inverted_pyramid.py": """for i in range(5, 0, -1):
    print(' '.join(str(x) for x in range(1, i+1)))
""",

    "pattern39_right_angle_star.py": """for i in range(1, 6):
    print(' '*(5-i) + '*'*i)
""",

    "pattern40_left_number_triangle.py": """for i in range(1, 6):
    print(' '.join(str(x) for x in range(1, i+1)))
""",

    "pattern41_star_hollow_triangle.py": """for i in range(1, 6):
    for j in range(1, i+1):
        if j==1 or j==i or i==5:
            print('*', end='')
        else:
            print(' ', end='')
    print()
""",

    "pattern42_upside_down_triangle.py": """for i in range(5, 0, -1):
    print('*'*i)
""",

    "pattern43_parallelogram.py": """for i in range(5):
    print(' '*i + '*'*5)
""",

    "pattern44_inverted_parallelogram.py": """for i in range(5):
    print(' '*(5-i) + '*'*5)
""",

    "pattern45_reverse_hollow_diamond.py": """for i in range(5, 0, -1):
    print(' '*(5-i) + '*' + ' '*(2*i-3) + ('*' if i>1 else ''))
""",

    "pattern46_inverted_hollow_pyramid.py": """for i in range(5, 0, -1):
    for j in range(1, 2*i):
        if j==1 or j==2*i-1 or i==5:
            print('*', end='')
        else:
            print(' ', end='')
    print()
""",

    "pattern47_full_hollow_diamond.py": """for i in range(1, 6):
    print(' '*(5-i) + '*' + ' '*(2*i-3) + ('*' if i>1 else ''))
for i in range(4, 0, -1):
    print(' '*(5-i) + '*' + ' '*(2*i-3) + ('*' if i>1 else ''))
""",

    "pattern48_rectangle_numbers.py": """for i in range(5):
    for j in range(1, 6):
        print(j, end=' ')
    print()
""",

    "pattern49_reverse_star.py": """for i in range(5, 0, -1):
    print('*'*i)
""",

    "pattern50_pyramid_numbers.py": """for i in range(1, 6):
    print(' '*(5-i) + ''.join(str(x) for x in range(1, i+1)))
"""
}
# Create files
for filename, code in patterns.items():
    with open(filename, "w") as f:
        f.write(code)

print("All 50 pattern files created successfully!")
