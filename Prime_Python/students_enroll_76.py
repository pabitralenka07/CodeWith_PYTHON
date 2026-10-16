# Lists students enrolled in English .

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Charlie", "Math"),
    ("Alice", "Science"),
    ("Bob", "Math"),
    ("Charlie", "English"),
    ("Alice","English"),
]

for name,course in info:
    if course == "English":
        print(name)
        