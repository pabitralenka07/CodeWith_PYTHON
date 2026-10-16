# Linear search

nums = [1,2,3,10,4]
x = 10
index = 0
for val in nums:
    if(val == x):
        print(f"{x} found at index = {index}")
        break
    index += 1
    