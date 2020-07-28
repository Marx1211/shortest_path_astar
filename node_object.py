from math import sqrt

class Node:

    def __init__(self, x, y, parent = None, children = None):
        self.x = x                  #X coordinate
        self.y = y                  #Y coordinate
        self.parent = parent        #Shortest path parent
        if children is None:        #Current node's children
            self.children = []
        self.f = 0                  #Total cost of the node
        self.g = 0                  #Distance to the start node
        self.h = 0                  #Estimated distance to end node

    #This method will calculate the g value
    def get_g(self):
        return self.parent.g + sqrt((self.x - self.parent.x)**2 + (self.y - self.parent.y)**2)
    #This method will calculate the h value
    def get_h(self, end):
        return sqrt((self.x - self.y)**2 + (end.x - end.y)**2)
    #This method will calculate the f value
    def get_f(self):
        return self.g + self.h
