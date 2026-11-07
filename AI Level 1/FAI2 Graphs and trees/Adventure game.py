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
        while len(Node.neighbors) != 0:
            prompt = input(Node.prompt)
            Node = self.graph[prompt]
        print(Node.prompt)

    def __str__(self):
        dummy = ""
        for key in self.graph:
            dummy += self.graph[key].__str__()+"\n\n"

        return dummy


start = Node("start","start of the story, option 1 or option 2(type go down path ()")

option1 = Node("go down path 1","Game over")

option2 = Node("go down path 2","path 2 leads to ..... choose option cat or dog(type go down path()")

option21 = Node("go down path cat","Game over")

option22 = Node("go down path dog","Spooky event, option leave or stay.(type go down path ()")

option23 = Node("go down path stay","YOU DED")

option24 = Node("go down path leave","you survived")

story = Graph()

story.add_node(start)

story.add_node(option1)

story.add_node(option2)

story.add_node(option21)

story.add_node(option22)

story.add_node(option23)

story.add_node(option24)

story.add_edge(start, option1)
story.add_edge(start, option2)
story.add_edge(option2, option21)
story.add_edge(option2, option22)
story.add_edge(option22, option23)
story.add_edge(option22, option24)

story.start_adventure(start)