def count_file_stats(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    words = content.split()

    num_words = len(words)
    num_chars = len(content)
    num_lines = len(content.splitlines())

    return num_words, num_chars, num_lines


# Main Program
filename = input("Enter file name: ")

w, c, l = count_file_stats(filename)

print(f"\n--- File Statistics for '{filename}' ---")
print(f"Words: {w} | Characters: {c} | Lines: {l}")