import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare value to current node
        # if value < self.value:
        #     # if smaller, go left
        #     if not self.left:
        #         self.left = BinarySearchTree(value)
        #     else:
        #         self.left.insert(value)
        # # if bigger, go right
        # else:
        #     if not self.right:
        #         self.right = BinarySearchTree(value)
        #     else:
        #         self.right.insert(value)
        if value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
            return
        elif value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
            return

        if value < self.value:
            self.left.insert(value)
        else:
            self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare value to the current node value
        if self.value == target:
            return True
        # if smaller, go left
        # if target < self.value:
        #     if not self.left:
        #         return False
        #     else:
        #         return self.left.contains(target)
        # if bigger, go right
        # else:
        #     if not self.right:
        #         return False
        #     else:
        #         return self.right.contains(target)

        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        
        # if self.left:
        #     return self.left.for_each(cb)
        # if self.right: 
        #     return self.right.for_each(cb)
        if self.left is not None:
            self.left.for_each(cb)
        
        cb(self.value)

        if self.right is not None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            node.in_order_print(node.left)

        print(node.value)

        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # uses queue data structure
        q = Queue()
        q.enqueue(node)
        visited = False
        
        while q is not None:
            if visited == False:
                q.dequeue()
                for i in range(q.len()):
                    visited = True
                    q.enqueue(i)
                    print(i)

        return q

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # uses stack data structure
        s = Stack()
        s.push(node)
        visited = False

        while s is not None:
            if visited == False:
                s.pop()
                for i in range(s.len()):
                    visited = True
                    s.push(i)
                    print(i)

        return s

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
