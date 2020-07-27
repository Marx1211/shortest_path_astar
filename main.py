import node.py

#Main function of the program. Opens a file and finds the shortest path from the start node to the end node.
def search_file(file_to_read):
    with open(file_to_read, 'r') as caves:
        for number in caves:
            graph = number.split(",")

        number_of_caverns = graph[0]
        start_cave = Node(1, graph[1], graph[2], None )
        end_cave = Node(30, graph[])
