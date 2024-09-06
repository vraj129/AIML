print("****************")
month = {
    "January":2200,
    "February":2350,
    "March":2000,
    "April":2130,
    "May":2190,
}

print(month["February"] - month["January"])

print("****************")
expense = 0
for i, (key,value) in enumerate(month.items()):
    if(i == 3):
        break
    expense += month[key]   

print(expense) 

print("****************")
for key,value in month.items():
    if(month[key] == 2000):
        print(f"You spend exactly 2000 in {key}" )
        break

print("****************")
month["June"] = 1980
month["April"] = month["April"] - 200
print(month["April"])


print("****************")
num = input("Enter number:\n")
num = int(num)
if(num < 0 or num == 0):
    print("invalid input")
else:
    for i in range(num):
        if(i % 2 != 0):
            print(i)