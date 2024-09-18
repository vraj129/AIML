class Node:
    def __init__(self,data = None,prev = None,next = None):
        self.data = data
        self.prev = prev
        self.next = next
    
class DoublyLinkedList: 
    def __init__(self):
        self.head = None

    def insertAtBegining(self,data):
        node = Node(data,None,self.head)
        self.head = node
    
    def insertAtEnd(self,data):
        if(self.head == None):
            node = Node(data,self.head,None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data,itr,None)
        itr.next = node

    def insertValues(self,values):
        self.head = None
        for data in values:
            self.insertAtEnd(data)
    
    def getLength(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count = count + 1
        
        return count
    
    def removeAt(self,index):
        if(index < 0 or index >= self.getLength()):
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        count = 0
        itr = self.head
        while itr:
            if(count == index - 1):
                if(count == self.getLength() - 2):
                    itr.next = None
                    break
                itr.next = itr.next.next
                itr.next.prev = itr
                break

            itr = itr.next
            count = count + 1
    
    def insertAt(self,index,data):
        if(index < 0 or index >= self.getLength()):
            raise Exception("Invalid index")
        
        if index == 0:
            self.insertAtBegining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if(count == index - 1):
                node = Node(data,itr,itr.next)
                itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count = count + 1

    def insertAfterValues(self,afterValue,value):
        if self.head is None:
            return
        
        count = 0
        itr = self.head
        while itr: 
            if(itr.data == afterValue):
                if(itr.next is None):
                    self.insertAtEnd(value)
                    break
                node = Node(value,itr,itr.next)
                itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count = count + 1

    def removeByValue(self,value):
        if self.head is None:
            return
        if self.head.data == value:
           if(self.head.next is None):
               self.head = None
               return
           self.head = self.head.next
           self.head.prev = None
           return
        
        itr = self.head
        count = 0
        while itr:
            if(itr.next != None and itr.next.data == value):
                if(count == self.getLength() - 2):
                    itr.next = None
                    break
                itr.next = itr.next.next
                itr.next.prev = itr
                break
            count = count + 1
            itr = itr.next

    def print(self):
        if self.head == None:
            print("Linked list is empty")
            return
        itr = self.head
        dllStr = ""
        while itr:
            dllStr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(dllStr)
    
    def printBackWard(self):
        if self.head == None:
            print("Linked list is empty")
            return
        lastNode = self.getLastNode()
        dllStr = ""
        while lastNode:
            dllStr += lastNode.data +'-->' 
            lastNode = lastNode.prev
        print(dllStr)
    
    def getLastNode(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insertValues(["banana","mango","grapes","orange"])
    dll.print()
    # dll.insertAfterValues("mango","apple")
    # dll.print()
    # dll.removeByValue("orange")
    # dll.print()
    # dll.removeByValue("figs")
    # dll.print()
    # dll.removeByValue("banana")
    # dll.removeByValue("mango")
    # dll.removeByValue("apple")
    # dll.removeByValue("grapes")
    dll.printBackWard()