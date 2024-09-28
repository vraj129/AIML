class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self,data):
        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def inOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTraversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inOrderTraversal()

        return elements

    def searchValue(self,val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.searchValue(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.searchValue(val)
            else:
                return False

def buildTree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.addChild(elements[i])
    return  root

if __name__ == "__main__":
    numbers = [17,4,1,20,9,23,18,34]
    numberTree = buildTree(numbers)
    print(numberTree.inOrderTraversal())
    print(numberTree.searchValue(44))
