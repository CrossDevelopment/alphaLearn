# BST Implementation 
# Need to implement the following:
    # search
    # remove 
    # add
    


class Node:
    rightChild,leftChild,data = None, None, None
    def __init__(self,key):
        self.leftChild = None
        self.rightChild = None
        self.data = key

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


