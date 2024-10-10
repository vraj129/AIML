
print("************")
expense = [2200,2350,2600,2130,2190]
print(expense[1]- expense[0])
print(expense[0]+expense[1]+expense[2])
print(2000 in expense)
expense.append(1980)
print(expense)
expense[3] = 2130 - 200
print(expense)

print("************")
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append("black panther")
print(heros)
heros.remove("black panther")
heros.insert(3,"black panther")
print(heros)
heros[1:3]=["Doctor Strange"]
print(heros)
heros.sort()
print(heros)