# from dll_stack import Stack
# from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the value is less than the root, move to the left
        if value < self.value:
            # if the left is empty
            if self.left is None:
                # add the node to the left
                self.left = BinarySearchTree(value)
                return
            else:
                # call the insert func and pass the value (recursion)
                return self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
                return
            else:
                # call the insert func and pass the value (recursion)
                return self.right.insert(value)
                

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if the target is equal to value, return true
        if target is self.value:
            return True
        # check if the value is less than the root, move to the left
        if target < self.value:
            if self.left is None:
                return False
            else:
                # call the contains func and pass the target (recursion)
                return self.left.contains(target)
        # check if the value is less than the root, move to the right
        if target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        # self.value is noe
        if self.value is None:
            return None
        # check if right value is none
        # pick the value as the highest
        if self.right is None:
            return self.value
        # call the get_max func on self.right (recursio)
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # if self.value is not None
        if self.value:
            # add the value to cb
            cb(self.value)
            # check if there is a left leaf, move to left           
            if self.left:
                # call the for_each func on self.left (recursio)
                self.left.for_each(cb)
            # check if there is a right leaf, move to right           
            if self.right:
               # call the for_each func on self.right (recursio)
                self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bb = BinarySearchTree(10)
bb.insert(20)
bb.insert(15)
