"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         self.size = len(self.storage)
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.insert(0, value)

#     def dequeue(self):
#         if self.storage == []:
#             return None
#         ret_value = None
#         for i in self.storage:
#             ret_value = i

#         self.storage.pop()
        
#         print("Length of the array", len(self.storage))
#         print("The array ", self.storage)
#         print("The returned value is ",ret_value)
#         return ret_value

class Queue:
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
            print("This is current: ", current)
            while current != self.storage.tail:
                count += 1
                current=current.get_next_node()
            return count+1

    def enqueue(self, value):
        self.storage.add_to_head(value)

    def dequeue(self):
        return self.storage.remove_tail()




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
