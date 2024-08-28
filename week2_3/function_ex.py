print("****************")
def areaOfTriangle(base,height,width = -1):
    if width != -1:
        return height * width
    return  1/2 *(base*height)

print(areaOfTriangle(base=10,height=10))
print(areaOfTriangle(base=10,height=10,width=10))

print("****************")
def printPattern(rows):
    if rows < 0:
        print("error")
    for i in range(1, rows + 1):
        t = ""
        for j in range(i):
            t += "*"
        print(t)


printPattern(rows=3)
printPattern(rows=4)
