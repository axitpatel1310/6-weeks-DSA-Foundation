class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def display(self):
        if self.head is None:
            return "Empty"
        current = self.head
        while current:
            print(current.data,end=" -> " )
            current = current.next
        print("None")
        
    def delete(self,data):
        if self.head is None:
            return "Empty"
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def update(self,node,data):
        if self.head is None:
            return "Empty"
        current = self.head
        while current:
            if current.data == node:
                current.data = data
                return
            current = current.next
            
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
"""
ll = LinkedList()
ll.add(5)
ll.add(6)
ll.add(7)
ll.display()
ll.reverse()
ll.display()
"""
