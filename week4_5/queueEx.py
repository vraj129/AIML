from collections import deque


class Queue: 
    def __init__(self): 
        self.buffer = deque()
    
    def enqueue(self,value):
        self.buffer.appendleft(value)
    
    def dequeue(self):
        return self.buffer.pop()

    def isEmpty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]
    
def printBinary(values):
    string =""
    q = Queue()
    for value in range(1,values + 1):
        t = decimalToBinary(value)
        q.enqueue(t)
        string += str(t) + "\n"
    return string

    

def decimalToBinary(value):
    return bin(value).replace("0b","")
    
if __name__ == "__main__":
    print(printBinary(10))