class HashTable:
    def __init__(self): 
        self.Max = 10
        self.arr = [None  for i in range(self.Max)]
    
    def getHash(self,key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.Max
    
    def __setitem__(self,key,value):
        k = self.getHash(key)
        if(self.arr[k] is None):
            self.arr[k] = (key,value)
        else:
            index = self.findSlot(k,key)
            self.arr[index] = (key,value)

    def findSlot(self,index,key):
        list = self.probeRange(index)
        for i in list:
            if(self.arr[i] is None or self.arr[i][0] == key):
                return i
        raise Exception("HashMemory full")

    def __getitem__(self,key):
        k = self.getHash(key)
        if(self.arr[k] is None):
            return
        list = self.probeRange(k)
        for i in list:
            if(self.arr[i] is None):
                return
            if(self.arr[i][0] == key):
                return self.arr[i][1]
    
    def __delitem__(self,key):
        k = self.getHash(key)
        if(self.arr[k] is None):
            return
        list = self.probeRange(k)
        for i in list:
            if(self.arr[i] is None):
                return
            if(self.arr[i][0] == key):
                self.arr[i] = None

    def probeRange(self,index):
        return [*range(index,self.Max)] + [*range(0,index)]


if __name__=="__main__":
    ht = HashTable()
    ht["march 6"] = 78
    ht["march 17"] = 110
    ht["march 8"] = 90
    print(ht.arr)
    del ht["march 6"]
    print(ht.arr)
    print(ht["march 6"])