import sys

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, node, edges):
        self.vertices[node] = edges

    def dijkstra_path(self, startNode, goalNode):
        unvisited  = {node: float("inf") for node in self.vertices.keys()}
        prevNodes = {node: None for node in self.vertices.keys()}
        path = []
        graph = self.vertices
        unvisited[startNode] = 0
        while self.vertices:
            currentNode = None
            for node in self.vertices:
                if currentNode == None:
                    currentNode = node
                elif unvisited[node] < unvisited[currentNode]:
                    currentNode = node

            for neighbourNode, distance in self.vertices[currentNode].items():
                newDistance = unvisited[currentNode] + distance
                if newDistance < unvisited[neighbourNode]:
                    unvisited[neighbourNode] = newDistance #setting new distance
                    prevNodes[neighbourNode] = currentNode #add seen node to list

            self.vertices.pop(currentNode)

        currentNode = goalNode
        while currentNode != startNode:
            try:
                path.append(currentNode)    #append node to path
                currentNode = prevNodes[currentNode] #get keyerror so break

            except KeyError:
                break

        path.append(startNode)

        if unvisited[goalNode] != float("inf"):
            path = path[::-1]
            pathString = ""
            for vertices in path:
                pathString += vertices + ", "
            print("The path from",startNode, "and", goalNode, "is ", pathString[:-2])
            print("The distance is: ", unvisited[goalNode])
        else:
            print("Not possible")

    def display_graph(self):
        print("Dictionary of the graph:",self.vertices, "\n")
        
    def __str__(self):
        return str(self.vertices)


if __name__ == '__main__':
    print("Dijkstra shortest path algorithm\n")
    
    g = Graph()
    g.add_vertex('A', {'B': 7, 'C': 8})
    g.add_vertex('B', {'A': 7, 'F': 2})
    g.add_vertex('C', {'A': 8, 'F': 6, 'G': 4})
    g.add_vertex('D', {'F': 8})
    g.add_vertex('E', {'H': 1})
    g.add_vertex('F', {'B': 2, 'C': 6, 'D': 8, 'G': 9, 'H': 3})
    g.add_vertex('G', {'C': 4, 'F': 9})
    g.add_vertex('H', {'E': 1, 'F': 3})
    g.display_graph()
    g.dijkstra_path('A', 'F')
