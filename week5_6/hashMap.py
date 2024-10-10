class HashTable: 
    def __init__(self): 
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    
    def getHash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self,key,value):
        k = self.getHash(key)
        found = False
        for index,ele in enumerate(self.arr[k]):
            if(len(ele) == 2 and ele[0] == key): 
                self.arr[k][index] = (key,value)
                found = True
                break
        if not found:
            self.arr[k].append((key,value))
    
    def __getitem__(self,key):
        k = self.getHash(key)
        for index,ele in enumerate(self.arr[k]):
            if(len(ele) == 2 and ele[0] == key):
                return ele[1]
        

    def __delitem__(self,key):
        k = self.getHash(key)
        for index,element in enumerate(self.arr[k]):
            if element[0] == key:
                del self.arr[k][index]

if __name__=="__main__":
    ht = HashTable()
    ht["march 6"] = 78
    ht["march 17"] = 110
    ht["march 8"] = 90
    print(ht.arr)
    del ht["march 6"]
    print(ht.arr)
    print(ht["march 6"])