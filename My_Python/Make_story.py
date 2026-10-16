def mad_libs():

    print("\nLet's create a story! Fill in the blanks.")

    noun = input("Noun: ")
    verb = input("Verb: ")
    adjective = input("Adjective: ")
    place = input("Place: ")

    story = f"""
Once upon a time, a {adjective} {noun}
decided to {verb} at the {place}.
Everyone was surprised, but it turned out
to be the best idea ever!
"""

    print("\nHere's your story:\n")
    print(story)


if __name__ == "__main__":
    mad_libs()
    