from node_object import Node


#Return a graph from a file. The parameter file_to_read should be a cav file in the defined format.
def create_graph(file_to_read):
    graph = []
    #Open file and split the data in it into a list
    with open(file_to_read, 'r') as caves:
        for number in caves:
            data = number.split(",")

        #Create the Nodes one by one from the data
        for cave in range(1, int(data[0]) + 1):
            node = Node(data[(cave * 2) - 1], data[cave * 2], None, None)
            graph.append(node)
            #Part of the data where connections start for each cave
            connections_start = (int(data[0]) * 2) + (int(data[0]) * (cave - 1))
            #Add all children to each node
            for number in range(1, int(data[0]) + 1):
                if(data[connections_start + number] == "1"):
                    node.children.append(number)
