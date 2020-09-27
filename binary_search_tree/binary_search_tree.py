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
from collections import deque
#Importing Stack#

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        if self.storage.head == None:
            return 0
        if self.storage.head == self.storage.tail:
            return 1
        else: 
            count = 0
            current = self.storage.head
            while current != self.storage.tail:
                count += 1
                current=current.get_next_node()
            return count+1

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        return self.storage.remove_head()
        

############# Importing LinkedList ################

class Node: 
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node

        else:
            new_node.set_next_node(self.head)
            self.head = new_node
        
    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node
    
    def remove_head(self):
        if self.head is None: 
            return None
        else:
            ret_value = self.head.get_value()

            if self.head == self.tail:
                self.head = None
                self.tail = None
            
            else: 
                self.head = self.head.get_next_node()
            return ret_value

    def remove_tail(self):
        if self.head is None:
            return None
        
        if self.head.get_next_node() == None:
            ret_value = self.head
            self.head = None
            self.tail = None
            return ret_value.get_value()

        current = self.head
        prev = current
        while current.get_next_node() is not None:
            prev = current
            current = current.get_next_node()
        ret_value = current    
        prev.set_next_node(None)
        return ret_value.get_value()
                

            

    def contains(self, value):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.get_value == value:
                return True
        return False

    def get_max(self):
        pass

###########################################

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = value
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else: 
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else: 
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            elif target == self.left:
                return True
            else:
                return self.left.contains(target)
        if target >= self.value:
            if self.right is None: 
                return False
            elif target == self.right:
                return True
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.value is None:
            return None
        if not self.right:
            return self.value
        return self.right.get_max()



        
                


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        qq = deque()
        qq.append(node)

        while len(qq) > 0:
            current = qq.popleft()
            print(current.value)
            if current.left:
                qq.append(current.left)
            if current.right:
                qq.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
         stack = Stack()
         stack.push(node)
         while stack.size != 0:
            node = stack.pop()
            print(node.value)
            if node.right:
                stack.push(node.right)
            if node.left:
                stack.push(node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print(bst)
bst.dft_print(bst)

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print(bst)
print("post order")
bst.post_order_dft(bst)  







