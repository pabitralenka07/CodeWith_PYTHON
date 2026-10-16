# Create dictionary of student and enrolled courses. 

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Charlie", "Math"),
    ("Alice", "Science"),
    ("Bob", "Math"),
    ("Charlie", "English"),
    ("Alice","English"),
]

dict = {}

for name,course in info:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)
