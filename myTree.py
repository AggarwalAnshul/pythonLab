class node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

class bst:
    def __init__(self):
        self.root = node()

    #inserts add elelments to the bst
    def insert(self, value):
        if self.root == None: #if the tree is empty
            self.root = node(value)
        else:
            self._insert(value, self.root) #private insert funcitons

    def _insert(self, value, cur_node):
        if value < cur_node.data:
            if cur_node.left == None:
                cur_node.left = node(value)
            else:                       #if more nodes down this level
                self.insert(value, self.cur_node.left_child)
        elif value > cur_node.data:
            if cur_node.right == None:
                cur_node.right = node(data)
            else:
                self._insert(value, self.cur_node.right)
        
        else: #to prevent duplication of data
            print('value already in tree !')


    #Prints the tree structure
    def print(self):
        if self.root:
            self._printTree(self.root)
    def _printTree(self, cur_node):
        if cur_node: #InOrder Traversal
            self._print(self,cur_node.left)
            print(self.cur_node.data)
            self._print(self,cur_node.right)
        
tree = bst()
