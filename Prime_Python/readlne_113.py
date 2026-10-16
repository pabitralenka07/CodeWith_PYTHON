f = open("code.txt","r") #Fle object

data = f.readline()

print(data)
print(type(data))
f.close()
