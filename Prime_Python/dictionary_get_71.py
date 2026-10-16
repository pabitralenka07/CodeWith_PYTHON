info = {
    "name":"pabitra",
    "cgpa":8.7,
    "subjects":["math","science"],
    3.14:"PI"
}

'''print(info.get("cgpa"))
print(info["cgpa2"])
This will give an error because "cgpa2" is not a key in the dictionary.'''


print(info.get("cgpa2"))
print("End of the program")
