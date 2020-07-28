from math import sqrt

class Node:

    def __init__(self, index, x, y, parent = None, children = None):
        self.index = index          #Node index
        self.x = x                  #X coordinate
        self.y = y                  #Y coordinate
        self.parent = parent        #Shortest path parent
        if children is None:        #Current node's children
            self.children = []
        self.f = 0                  #Total cost of the node
        self.g = 0                  #Distance to the start node
        self.h = 0                  #Estimated distance to end node

    #This method will calculate the g value
    def set_g(self):
        self.g = self.parent.g + sqrt((self.x - self.parent.x)**2 + (self.y - self.parent.y)**2)
    #This method will calculate the h value
    def set_h(self, end):
        self.h = sqrt((self.x - end.x)**2 + (self.y - end.y)**2)
    #This method will calculate the f value
    def set_f(self):
        self.f = self.g + self.h
