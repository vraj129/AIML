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
    
    def preOrderTraversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preOrderTraversal()
        if self.right:
            elements += self.right.preOrderTraversal()
        return elements
    
    def postOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.preOrderTraversal()
        if self.right:
            elements += self.right.preOrderTraversal()
        elements.append(self.data)
        return elements

    def findMin(self):
        if self.left is None:
            return  self.data
        return  self.left.findMin()

    def findMax(self):
        if self.right is None:
            return  self.data
        return  self.right.findMax()

    def calculateSum(self):
        sumValue = 0
        if self.left:
            sumValue += self.left.calculateSum()
        sumValue += self.data
        if self.right:
            sumValue += self.right.calculateSum()
        return  sumValue

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
    numbers = [15,12,7,14,27,20,23,88]
    numberTree = buildTree(numbers)
    print(numberTree.inOrderTraversal())
    print(numberTree.searchValue(1))
    print(numberTree.findMin())
    print(numberTree.findMax())
    print(numberTree.calculateSum())
    print(numberTree.preOrderTraversal())
    print(numberTree.postOrderTraversal())
