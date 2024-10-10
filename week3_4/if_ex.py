print("*****************")
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
cityName = input("Enter city name\n")
if cityName in india:
    print(f"{cityName} is in India")
elif cityName in pakistan:
    print(f"{cityName} is in pakistan")
else:
    print(f"{cityName} is in bangladesh")

print("***********************")
cityName1 = input("Enter city name1\n")
cityName2 = input("Enter city name2\n")
if cityName1 in india and cityName2 in india:
    print("Both cities are in India")
elif cityName1 in pakistan and cityName2 in pakistan:
    print("Both cities are in Pakistan")
else:
    print("Both cities are in Bangladesh")

print("***********************")
sugarLevel = input("Enter sugar level:\n")
sugarLevel = int(sugarLevel)
if sugarLevel > 100:
    print("High")
elif 100 >= sugarLevel >= 80:
    print("normal")
else:
    print("low")
