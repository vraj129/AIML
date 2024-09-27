from collections import deque
import threading
import time


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

def foodOrder(q,orders):
    for order in orders:
        time.sleep(0.5)
        q.enqueue(order)

def serveFood(q):
    for i in range(q.size()):
        time.sleep(2)
        print(q.dequeue())
    

if __name__ == "__main__":
    q = Queue()
    print(printBinary(10))
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=foodOrder(q,orders))
    t2 = threading.Thread(target=serveFood(q))
    t1.start()
    time.sleep(1)
    t2.start()

    
    t1.join()
    t2.join()

