"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         self.size = len(self.storage)
#         return len(self.storage)

#     def push(self, value):
#         self.storage.insert(0, value)

#     def pop(self):
#         if self.storage == []:
#             return None
#         else: 
#             ret_value = self.storage[0]
#             self.storage.pop(0)
#             return ret_value

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

