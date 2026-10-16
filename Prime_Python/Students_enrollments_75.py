# List all courses

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Charlie", "Math"),
    ("Alice", "Science"),
    ("Bob", "Math"),
    ("Charlie", "English"),
    ("Alice","English"),
]

courses_set = set()
for tup in info:
    courses_set.add(tup[1])
print(courses_set)
