#trees

class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def prints(self):
        print(self.data)

class bst:
    def __init__(self):
        self.root=None
        node().__init__()
    
    def ins(self,data):
        if self.root==None:
            self.root=node(data)
        else:
            self.insert(data,self.root)
    def insert(self,data,cur_node):
        if data<cur_node.data:
            if cur_node.left==None:
                cur_node.left=node(data)
            else:
                self.insert(data,cur_node.left)
        elif data>cur_node.data:
            if cur_node.right==None:
                cur_node.right=node(data)
            else:
                self.insert(data,cur_node.right)
            
        else:
            print("value already in tree")

    def show(self):
        if self.left:
            self.left.show()
        print(self.data),
        if self.right:
            self.right.show()


    def find(self, value):
        if self.root:
            return self._find(self, value, self.root)
        else:
            return None
    def _find(self, value, cur_node):
        if cur_node.data == value:
            return cur_node
        elif (value < cur_node.data and cur_node.left != None):
            return self._find(value, cur_node.left)
        elif (value > cur_node.data and cur_node.right !=None): 
            return self._find(value, cur_node.right)
        else:
            return False
    def delete(self, value):
        
        
    def delete(self):
#inserting values into tree

