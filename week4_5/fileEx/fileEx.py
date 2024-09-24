print("***************")
arr = []
f = open("path to the file","r")
for line in f:
    words = line.split(",")
    try:
        arr.append(int(words[1]))
    except:
        print("Invalid Row")
print(f"Average temp in first week: {sum(arr[0:7])/7}")
print(f"Max temperature: {max(arr[0:10])}")

print("*****************")
weather = {}
f = open("path to the file","r")
for line in f: 
    words = line.split(",")
    try:
        weather[words[0]] = int(words[1])
    except:
        print("Invalid row")
print(weather["Jan 9"])
print(weather["Jan 4"])

print("**************")
poem = {}
f = open("path to the file","r")
for line in f:
    words = line.split(" ")
    for word in words:
        word = word.replace("\n","")
        if(word in poem):
            poem[word] += 1
        else:
            poem[word] = 1

print(poem)