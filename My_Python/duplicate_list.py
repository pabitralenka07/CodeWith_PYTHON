def remove_duplicates(lst):
    unique_list = []

    for item in lst:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


# Taking input from user
numbers = list(map(int, input("Enter numbers: ").split()))

print(
    "List after removing duplicates:",
    remove_duplicates(numbers)
)
