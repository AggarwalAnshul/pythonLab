class node:
    def __init__(self, data = None):
        self.data = data
        self.right = None
        self.left = None

class bst:
    def __init__(self, data = None):
        self.root = node(data)

    #Inserts the node in the Tree
    def insert(self, data):
        if self.root is None:
            self.root = node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, cur_node, data):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = node(data)
            else:
                self._insert(cur_node.left, data)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = node(data)
            else:
                self._insert(cur_node.right, data)
        else:
            print("Data Duplication is not allowed in BST")

    #Prints the tree
    def prints(self):
        if self.root is None:
            print("Tree is empty")
        else:
            self._prints(self.root)
    def _prints(self, cur_node):
        if cur_node:
            self._prints(cur_node.left)
            print(cur_node.data, end=' ')
            self._prints(cur_node.right)


    #Finds the element in the tree
    def find(self,data):
        if self.root is not None:
            self._find(self.root, data)
        else:
            print("Tree is empty")
    def _find(self, cur_node, data):
        if cur_node is not None:
            if cur_node.data == data:
                print("True")
                return True
            elif data > cur_node.data:
                self._find(cur_node.right, data)
            elif data < cur_node.data:
                self._find(cur_node.left, data)
            else:
                return False

    def findMinNode(self, cur_node):
        cur = cur_node
        while(cur.left is not None):
            cur = cur.left
        return cur

    #Deletes the node form the tree adn returns the new node
    def delete(self, roots, data):
        if roots is None:
            return roots
        if data > roots.data:
            roots.right = self.delete(roots.right, data)
        elif data < roots.data:
            roots.left = self.delete(roots.left, data)
        else:
            if roots.left is None:
                temp = roots.right
                roots = None
                return temp
            elif roots.right is None:
                temp = roots.left
                roots = None
                return temp
            temp = self.findMinNode(roots.right)
            roots.data = temp.data
            roots.right = self.delete(roots.right, temp.data)

        return roots


tree = bst(10)
tree.insert(1)
tree.insert(5)
tree.insert(20)
tree.insert(30)

            
