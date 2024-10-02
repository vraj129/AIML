class Graph:
    def __init__(self,edges): 
        self.edges = edges
        self.graphDict = {}
        for start,end in self.edges:
            if start in self.graphDict:
                self.graphDict[start].append(end)
            else:
                self.graphDict[start] = [end]
        print(self.graphDict)
    
    def getPaths(self,start,end,path = []):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graphDict:
            return []
        
        paths = []
        for node in self.graphDict[start]:
            if node not in path:
                newPath = self.getPaths(node,end,path)
                for p in newPath:
                    paths.append(p)
        return paths
    
    def getShortestPath(self,start,end,path = []):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graphDict:
            return None

        shortestPath = None
        for node in self.graphDict[start]:
            if node not in path:
                sp = self.getShortestPath(node,end,path)
                if sp:
                    if shortestPath is None or len(sp) < len(shortestPath):
                        shortestPath = sp
        return shortestPath 

if __name__ == "__main__":
    routes = [
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Paris","New York"),
        ("Dubai","New York"),
        ("New York","Toronto"),
    ]
    graph = Graph(routes)
    start = "Mumbai"
    end = "New York"
    # print(graph.getPaths(start,end))
    print(graph.getShortestPath(start,end))