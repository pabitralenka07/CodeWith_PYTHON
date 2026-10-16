f = open("code.txt","r") #Fle object

data = f.read()

print(data)
print(type(data))
f.close()
