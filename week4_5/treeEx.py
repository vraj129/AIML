class TreeNode:
    def __init__(self,data,designation):
        self.parent = None
        self.children = []
        self.data = data
        self.designation = designation
    
    def addChild(self,child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def printTree(self,type):
        if(type == "name"):
            spaces = " " * self.getLevel() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data)
            if self.children:
                for child in self.children:
                    child.printTree(type)
        elif type == "designation":
            spaces = " " * self.getLevel() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.designation)
            if self.children:
                for child in self.children:
                    child.printTree(type)
        else:
            spaces = " " * self.getLevel() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data + " ("+self.designation+")")
            if self.children:
                for child in self.children:
                    child.printTree(type)


class TreeNodeLocation:
    def __init__(self, data):
        self.parent = None
        self.children = []
        self.data = data

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, type):
        if (self.getLevel() <= type):
            spaces = ' ' * self.getLevel() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data)
            if self.children:
                for child in self.children:
                    child.print_tree(type)


def buildManagementTree():
    root = TreeNode("Nilupul","CEO")

    ctoNode = TreeNode("Chinmay","CTO")

    infraNode = TreeNode("Vishwa","Infrastructure Head")

    cloudNode = TreeNode("Dhaval","Cloud Manager")
    appNode = TreeNode("Abhijit","App Manager")
    infraNode.addChild(cloudNode)
    infraNode.addChild(appNode)

    applicationNode = TreeNode("Aamir","Application Head")
    ctoNode.addChild(infraNode)
    ctoNode.addChild(applicationNode)

    hrNode = TreeNode("Gels","HR Head")

    recNode = TreeNode("Peter","Recruitment Manager")
    policyNode = TreeNode("Waqas","Policy Manager")

    hrNode.addChild(recNode)
    hrNode.addChild(policyNode)

    root.addChild(ctoNode)
    root.addChild(hrNode)

    return root



def buildLocationTree():
    root = TreeNodeLocation("Global")

    indiaNode = TreeNodeLocation("India")
    usaNode = TreeNodeLocation("USA")

    gujaratNode = TreeNodeLocation("Gujarat")

    amdNode = TreeNodeLocation("Ahmedabad")
    barodaNode = TreeNodeLocation("Vadodara")

    gujaratNode.addChild(amdNode)
    gujaratNode.addChild(barodaNode)

    karNode = TreeNodeLocation("Karnataka")

    bangNode = TreeNodeLocation("Bengaluru")
    mysoreNode = TreeNodeLocation("Mysore")
    karNode.addChild(bangNode)
    karNode.addChild(mysoreNode)

    indiaNode.addChild(gujaratNode)    
    indiaNode.addChild(karNode)

    njNode = TreeNodeLocation("New Jersey")
    princeNode = TreeNodeLocation("Princeton")
    trentNode = TreeNodeLocation("Trenton")
    njNode.addChild(princeNode)
    njNode.addChild(trentNode)

    calNode = TreeNodeLocation("California")
    sfNode = TreeNodeLocation("San francisco")
    mvNode = TreeNodeLocation("Mountain View")
    palNode = TreeNodeLocation("Palo Alto")

    calNode.addChild(sfNode)
    calNode.addChild(mvNode)
    calNode.addChild(palNode)

    usaNode.addChild(njNode)
    usaNode.addChild(calNode)

    root.addChild(indiaNode)
    root.addChild(usaNode)
    return root    

if __name__ == "__main__":
#    root =  buildManagementTree()
#    root.printTree("name")
#    root.printTree("designation")
#    root.printTree("both")

    root = buildLocationTree()
    root.print_tree(1)
    root.print_tree(2)
    root.print_tree(3)