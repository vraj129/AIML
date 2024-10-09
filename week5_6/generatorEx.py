def squareNumber(): 
    a = 0
    while True:
        a += 1
        yield a * a

if __name__ == "__main__":
    for s in squareNumber():
        if s > 100:
            break
        print(s)