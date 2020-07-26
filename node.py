from math import sqrt

class Node:

    def __init__(self, index, x, y, parent = None):
        self.index = index          #Node number
        self.x = x                  #X coordinate
        self.y = y                  #Y coordinate
        self.parent = parent        #Shortest path parent
        self.f = 0                  #Total cost of the node
        self.g = 0                  #Distance to the start node
        self.h = 0                  #Estimated distance to end node

    #This method will calculate the g value
    def get_g(self):
        return self.parent.g + sqrt((self.x - self.parent.x)**2 + (self.y - self.parent.y)**2)

    def get_h(self, end):
        return sqrt((self.x - self.y)**2 + (end.x - end.y)**2)

    def get_f(self):
        return self.g + self.h
