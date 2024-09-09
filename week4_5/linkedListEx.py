class Node:
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self,data):
        if(self.head is None):
            node = Node(data,None)
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self,index):
        if(index < 0 or index >= self.get_length()):
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if(count == index - 1):
                itr.next = itr.next.next
                break
             
            itr = itr.next
            count += 1
           
    def insert_at(self,index,data):
        if(index < 0 or index >= self.get_length()):
            raise Exception("Invalid Index")
        
        if(index == 0):
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if(count == index - 1):
                node = Node(data,itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
   
        if self.head is None:
            return
        
        if self.head.data == data_after:
            node = Node(data_to_insert,self.head.next)
            self.head.next = node
            return

        itr = self.head
        while itr:
            if(itr.data == data_after):
                node = Node(data_to_insert,itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
           self.head = self.head.next
           return
        
        itr = self.head
        while itr:
            if(itr.next != None and itr.next.data == data):
                itr.next = itr.next.next
                break
            itr = itr.next


    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count
    
    def print(self):
        if(self.head is None):
            print("Linked list is empty")
            return
        llstr = ""
        itr = self.head
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
