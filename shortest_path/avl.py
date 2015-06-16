
import bst

def height(node):
    if node is None:
        return -1
    else:
        return node.height

def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1   


class AVL(bst.BST):
    """
AVL binary search tree implementation.
Supports insert, find, and delete-min operations in O(lg n) time.
"""
    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)

    def insert(self, t):
        """Insert key t into this tree, modifying it in-place."""
        node = bst.BST.insert(self, t)
        self.rebalance(node)

    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    def find_smallest(self, start_node):
        node = start_node
        while node.left:
            node = node.left
        return node

    def delete_min(self):
        node, parent = bst.BST.delete_min(self)
        self.rebalance(parent)
        return node

    def remove(self, node):

        if not node is None:
            #Node is a leaf
            if node.right == None and node.left == None:
                self.remove_leaf(node)
            elif (bool(node.right) ^ bool(node.left)):
                self.remove_branch(node)
            else:
                self.swap_with_sucessor_and_remove(node)

    def remove_leaf(self, node):
        print
        parent = node.parent
        if(parent):
            if(not parent.left == None and parent.left.key == node.key and parent.left.label == node.label):
                #print("===> Setting parent left to none")
                parent.left = None
            else:
                parent.right = None
            parent.height = max(height(parent.left), height(parent.right)) + 1 
        else:
            self.root = None
        node.disconnect()

        node = parent
        while(node):
            balance = (node.left.height if node.left else -1) - (node.right.height if node.right else -1)
            if not balance in [-1, 0, 1]:
                self.rebalance(node)
            node = node.parent


    def remove_branch(self, node):
        parent = node.parent
        if (parent):
            if parent.left.key == node.key and parent.left.label == node.label:
                parent.left = node.right or node.left
            else:
                parent.right = node.right or node.left
            if node.left:
                node.left.parent = parent
            else:
                node.right.parent = parent 
            parent.height = max(height(parent.left), height(parent.right)) + 1 
        node.disconnect()
        # rebalance
        node = parent
        while(node):
            balance = (node.left.height if node.left else -1) - (node.right.height if node.right else -1)
            if not balance in [-1, 0, 1]:
                self.rebalance(node)
            node = node.parent

    def swap_with_sucessor_and_remove (self, node):
        #print("===> Node to remove: {0}".format(node.label))

        successor = self.find_smallest(node.right)

        #print("===> Node sucessor: {0}".format(successor.label))
        self.swap_nodes (node, successor)

        if node.height == 0:
            self.remove_leaf(node)
        else:
            self.remove_branch(node)
            
    def swap_nodes (self, node1, node2):
        parent1 = node1.parent #20.6
        left1 = node1.left #13.5
        right1 = node1.right #20.4
        parent2 = node2.parent #20.3
        left2 = node2.left #None
        right2 = node2.right #None
        
        # swap heights
        tmp = node1.height #1
        node1.height = node2.height #0
        node2.height = tmp #1
       
        if not parent1 == None:
            if (not parent1 == None) and parent1.left.key == node1.key and parent1.left.label == node1.label:
                parent1.left = node2
            else:
                parent1.right = node2
            node2.parent = parent1
        else:
            self.rootNode = node2
            node2.parent = None

        node2.left = left1
        left1.parent = node2
        node1.left = left2 # None
        node1.right = right2
        if not right2 == None:
            right2.parent = node1 
        if not (parent2.key == node1.key and parent2.label == node1.label):
            node2.right = right1
            right1.parent = node2
            
            parent2.left = node1
            node1.parent = parent2
        else:
            node2.right = node1
            node1.parent = node2  

        if not self.root == None and (self.root.key == node1.key and self.root.label == node1.label):
            self.root = node2


    def find(self,t):
        t_key = t[0]
        t_label = t[1]
        node = bst.BST.find(self,t_key,t_label)
        return node