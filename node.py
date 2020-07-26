
class Node:

    def __init__(self, index, x, y, parent, children):
        self.index = index          #Node number
        self.x = x                  #X coordinate
        self.y = y                  #Y coordinate
        self.parent = parent        #Shortest path parent
        self.children = children    #Connected children Nodes
        self.f = self.g + self.h    #Total cost of the node
        self.g = get_g()            #Distance to the start node
        self.h = get_h()            #Estimated distance to end node

    #This method will calculate the distance to the start node
    def get_g(distance):
        f = 
