def checkNumber(func):
    def wrapper(x):
        if type(x) == int and x > 0:
            return func(x)
        else: 
            raise Exception("Invalid number")
    return wrapper

@checkNumber
def calcFactorial(number):
    if number == 1:
        return 1
    else: 
        return number * calcFactorial(number - 1)
        

print(calcFactorial(10))
print(calcFactorial(-10))
