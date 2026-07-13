#Problem 1,2,3,4 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None 
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def update(self,data,new):
        if self.head is None:
            print("Empty")
            return
        current = self.head
        while current:
            if current.data == data:
                current.data = new
            current = current.next
    def delete(self,data):
        if self.head is None:
            print("Empty")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.data == data:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        print("Data Not Found")
    def display(self):
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print("None")
    def insert_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
     
ll = LinkedList()
ll.insert(12)
ll.insert(24)
ll.insert(36)
ll.display()
ll.update(12,10)
ll.display()
ll.delete(24)
ll.display()
ll.insert_start(24)
ll.display()

