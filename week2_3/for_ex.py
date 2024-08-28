print("****************")
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
headCount = 0
for i in result:
    if i == "tails":
        continue
    headCount += 1
print(headCount)

print("****************")
for i in range(1,11):
    if i%2 == 0:
        continue
    print(i*i)

print("****************")
month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
t = input("Enter the amount to be found :\n")
expense = int(t)
for i in range(len(expense_list)):
    if expense_list[i] == expense:
        print(f"Expense found in month {month_list[i]} and the expense is {expense}")
        break
    elif i == len(expense_list) - 1:
        print("Expense not found")

print("****************")
for i in range(1,6):
    if i > 0:
        answer = input("Are you tired ?\n")
        if answer.lower() == "yes":
            print("you didn't finish the race")
            break
        else:
            continue
    elif i == 5:
        print("Congratulations you finished the race")

print("****************")
for i in range(1,6):
    t = ""
    for j in range(i):
        t +="*"
    print(t)