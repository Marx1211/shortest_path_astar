from node_object import Node


#Return a graph from a file. The parameter file_to_read should be a cav file in the defined format.
def create_graph(file_to_read):
    graph = []
    #Open file and split the data in it into a list
    with open(file_to_read, 'r') as caves:
        for number in caves:
            data = [int(n) for n in number.split(",")]
        #Create the Nodes one by one from the data
        for cave in range(1, data[0] + 1):
            node = Node(cave, data[(cave * 2) - 1], data[cave * 2], None, None)
            #Part of the data where connections start for each cave
            connections_start = (data[0] * 2) + cave
            #Add all children to each node
            for connection in range(connections_start, data[0] * data[0], data[0]):
                if(data[connection] == 1):
                    node.children.append(divmod(connection, 30)[0] - 1)
            graph.append(node)
    return graph

