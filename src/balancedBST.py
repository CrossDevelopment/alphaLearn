# BST Implementation 
# Need to implement the following:
    # search
    # remove 
    # add
    


class Node:
    rightNode,leftNode,node = None, None, None
    def __init__(self,key):
        self.leftNode = None
        self.rightNode = None
        self.node = key

class Tree: 
    root = None 
    size = 0
    def __init__(self):
        self.size = 0
        self.root = None
        
    def insert(self,node,num):
        return
    def remove(self,node,num):
        return 
    def search(self,node,num):
        return
    def print_tree(self)

