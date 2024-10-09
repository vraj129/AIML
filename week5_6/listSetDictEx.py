def zipBinary():
    integer = [0, 1, 2, 3, 4]
    binary = ["0", "1", "10", "11", "100"]
    binaryDict = {i:b for i,b in zip(integer,binary)}
    print(binaryDict)

def additiveInverse():
    integer = [1, -1, 2, 3, 5, 0, -7]
    aI = [i * -1 for i in integer ]
    print(aI)

def uniqueSquare():
    integer = [1, -1, 2, -2, 3, -3]
    sqSet = {i*i for i in integer}
    print(sqSet)

if __name__ == "__main__":
    zipBinary()
    additiveInverse()
    uniqueSquare()
    set1 = {1,2,3,4,5}
    set2 = {4,5,6,7,8}
    print(set1 - set2)
        