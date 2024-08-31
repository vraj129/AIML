import math


print("**********")
countries = {"China":143,"India":136,"USA":32,"Pakistan":21}
answer = input("Input :\n")
if(answer.lower() == "print"):
    for k,v in countries.items():
        print(f"{k} ==> {v}")
elif answer.lower() == "add":
    country = input("Enter country name:\n")
    if(country in countries):
        print("Country already exist")
    else:
        population = input(f"Enter population for {country}:\n")
        countries[country] = population
        for k,v in countries.items():
            print(f"{k} ==> {v}")
elif answer.lower() == "remove":
    country = input("Enter country name to remove:\n")
    if country in countries: 
        del countries[country]
        for k,v in countries.items():
            print(f"{k} ==> {v}")
    else: 
        print("Country does not exist")
elif answer.lower() == "query":
    country = input("Enter country name:\n")
    if(country in countries):
        print(f"Population in {country} is {countries[country]}")
    else:
        print("Country does not exist")   


print("**********")
stocks = {
    "info":[600,630,620],
    "ril":[1430,1490,1567],
    "mtl":[234,180,160]
}

answer = input("Enter input:\n")
if answer.lower() == "print":
    for k,v in stocks.items():
        avg = 0
        for i in v:
            avg += i
        print(f"{k} ==> {v} ==> avg: {round(avg/len(v),2)}")
elif answer.lower() == "add":
    stock = input("Enter stock:\n")
    price = input(f"Enter {stock} price:\n")
    price = float(price)
    if(stock in stocks):
        t = stocks[stock]
        t.append(price)
        stocks[stock] = t
        for k,v in stocks.items():
            avg = 0
            for i in v:
                avg += i
            print(f"{k} ==> {v} ==> avg: {round(avg/len(v),2)}")
    else:
        stocks[stock] = [price]
        for k,v in stocks.items():
            avg = 0
            for i in v:
                avg += i
            print(f"{k} ==> {v} ==> avg: {round(avg/len(v),2)}")

print("**********")
def circle_calc(radius):
    return math.pi * (radius**2),2*math.pi*radius,radius+radius

def main():
    radius = input("Enter radius:\n")
    radius = float(radius)
    area,circumference,diameter = circle_calc(radius)
    print(f"Area: {area}, Circumference: {circumference}, Diameter: {diameter}")
main()