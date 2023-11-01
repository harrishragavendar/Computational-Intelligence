from queue import PriorityQueue

class Node:
    def __init__(self, data, heuristic):
        self.data = data
        self.neighbors = []
        self.heuristic = heuristic
        self.g_cost = float('inf')

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node, heuristic):
        self.nodes[node] = Node(node, heuristic)

    def add_edge(self, start, end, cost):
        self.nodes[start].neighbors.append((end, cost))
        self.nodes[end].neighbors.append((start, cost))
    
    def astar(self, start, goal):
        visited = set()
        pq = PriorityQueue()
        pq.put((0 + self.nodes[start].heuristic, 0, [start]))

        while not pq.empty():
            current_cost, g_cost, current_path = pq.get()
            print(f"\nChosen path: {' -> '.join(current_path)} \t Cost: {current_cost}")
            current_vertex = current_path[-1]

            if current_vertex == goal:
                return current_cost, current_path

            if current_vertex in visited:
                continue

            visited.add(current_vertex)
            current_node = self.nodes[current_vertex]

            intermediate_paths = []

            for neighbor, cost in current_node.neighbors:
                new_g_cost = g_cost + cost
                if neighbor in visited:
                    self.nodes[neighbor].g_cost = min(self.nodes[neighbor].g_cost, new_g_cost)

                else:
                    new_cost = new_g_cost + self.nodes[neighbor].heuristic
                    new_path = current_path + [neighbor]
                    pq.put((new_cost, new_g_cost, new_path))
                    intermediate_paths.append((new_cost, new_path))

            print(f"Possible paths from {current_vertex}:")
            for cost, path in intermediate_paths:
                print(f"{' -> '.join(path)} \t Cost: {cost}")
        return float('inf'), None
    
graph = Graph()

# Sample testcase, Graph is in testcase.png
# graph.add_node('a', 14)
# graph.add_node('b', 12)
# graph.add_node('c', 11)
# graph.add_node('d', 6)
# graph.add_node('e', 4)
# graph.add_node('f', 11)
# graph.add_node('z', 0)

# graph.add_edge('a', 'b', 4)
# graph.add_edge('a', 'c', 3)
# graph.add_edge('b', 'e', 12)
# graph.add_edge('b', 'f', 5)
# graph.add_edge('c', 'd', 7)
# graph.add_edge('c', 'e', 10)
# graph.add_edge('d', 'e', 2)
# graph.add_edge('e', 'z', 5)
# graph.add_edge('f', 'z', 16)

while(True):
    print("\n=======MENU=======")
    print("1 -> Add Node")
    print("2 -> Add Edge")
    print("3 -> A-Star Search")
    print("4 -> Exit")
    print("==================\n")
    choice = int(input("Enter choice: "))

    if(choice==1):
        node=input("Enter node: ")
        heuristic=int(input("Enter heuristic: "))
        graph.add_node(node, heuristic)

    elif(choice==2):
        node1=input("Enter node 1: ")
        node2=input("Enter node 2: ")
        cost=int(input("Enter cost: "))
        graph.add_edge(node1, node2, cost)
    
    elif(choice==3):
        source = input("Enter source node: ")
        goal = input("Enter goal node: ")
        cost, path = graph.astar(source, goal)
        if path is not None:
            print(f"\nOptimal path: {' -> '.join(path)}")
            print(f"Optimal cost: {cost}")
        else:
            print("No path found to goal node.")

    elif(choice==4):
        break

    else:
        print("Enter a valid choice!")
