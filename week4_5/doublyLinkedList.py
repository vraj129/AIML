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

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insertAtBegining("tt")
    dll.insertAtEnd("tt1")
    dll.insertAtEnd("tt2")
    dll.print()