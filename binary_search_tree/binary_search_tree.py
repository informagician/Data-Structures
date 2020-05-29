"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if value is None
        if value is None:
            return
        # check if tree has a root
        if self.value is None:
            self.value = BSTNode(value)
        
        # insert in left or right
        if self.value >= value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif self.value < value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if target exists
        if target is None:
            return False
        
        # check if tree exists
        if self.value is None:
            return False
        
        # check all the other conditions
        if self.value == target:
            return True
        elif self.value > target:
            if self.left:
                if self.left == target:
                    return True
                else:
                    return self.left.contains(target)
        elif self.value < target:
            if self.right:
                if self.right == target:
                    return True
                else:
                    return self.right.contains(target)
                

    # Return the maximum value found in the tree
    def get_max(self):
        # check if tree exists
        if self.value is None:
            return None
        # check right
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.value:
            fn(self.value)

        if self.right:
            self.right.for_each(fn)
        
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        # print: left-root-right
        # is it the most bottom-left node?
        
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)
            



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node is None:
            return
        queue = []

        queue.append(node)

        while(len(queue) > 0):
            
            print(queue[0].value)
            current = queue.pop(0)


            if current.left is not None:
                queue.append(current.left)
            
            if current.right is not None:
                queue.append(current.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Preorder Traversal
        
        if node is None:
            return
        
        print(node.value)
        if node.left:
            self.dft_print(node.left)

        if node.right:
            self.dft_print(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node is None:
            return
        
        print(node.value)
        if node.left:
            self.dft_print(node.left)
            
        if node.right:
            self.dft_print(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is None:
            return

        if node.left:
            self.post_order_dft(node.left)
        elif node.right:
            self.post_order_dft(node.right)
        else:
            print(node.value)
        
