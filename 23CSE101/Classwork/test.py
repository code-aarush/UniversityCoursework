keys = []
f = open("demo.csv", "r")
keytitle = f.readline()
print(keytitle)
word = ""
for i in range(len(keytitle)):
    if keytitle[i] != "," :
        word += keytitle[i]
        print(word)
    elif keytitle[i] == ",": 
        keys.append(word)
        word = ""

keys.append(word)

print(keys)

nextline = f.readline()
print(nextline)