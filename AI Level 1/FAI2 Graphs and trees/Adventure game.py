class Node:
    def __init__(self,key,prompt):
        self.key = key
        self.neighbors = []
        self.prompt = prompt
    def add_neighbor(self,Node):
        self.neighbors.append(Node)
    def __str__(self):

        dummy = f"Id:{self.key} , Neighbors:"
        for i in self.neighbors:
            dummy += i.key + ", "
        return dummy
class Graph:
    def __init__(self):
        self.graph = {}
    def add_node(self,Node):
        self.graph[Node.key] = Node
    def add_edge(self,Node1,Node2):
        if not Node1.key in self.graph:
            print(f'Node{Node1.key} is not in the graph')
        elif not Node2.key in self.graph:
            print(f'Node{Node2.key} is not in the graph')
        else:
            Node1.add_neighbor(Node2)
    def start_adventure(self,Node):
        print(Node.prompt)
        if len(Node.neighbors) = 0:
            

    def __str__(self):
        dummy = ""
        for key in self.graph:
            dummy += self.graph[key].__str__()+"\n\n"

        return dummy