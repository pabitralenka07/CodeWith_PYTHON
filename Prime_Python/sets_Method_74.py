s = {1,3,2,3,4,6,5,3,2,4,4}

s.add(7)
print(s)

s.remove(3)
print(s)

s.clear()
print(s)

s.pop()
print(s)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
