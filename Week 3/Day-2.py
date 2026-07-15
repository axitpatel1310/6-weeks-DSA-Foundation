class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
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
            return "Nothing to show"
        current = self.head
        while current:
            print(current.data,end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        if self.head is None:
            return
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def mid_ele(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
        
    def remove_nth_from_end(self,n):
        dummy = Node(0)
        dummy.next = self.head
        slow = dummy
        fast = dummy
        
        for _ in range(n+1):
            if fast is None:
                return 
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        self.head = dummy.next
    
    def reverse_between(self, left, right):
    if not self.head or left == right:
        return

    dummy = Node(0)
    dummy.next = self.head

    prev = dummy

    # Move prev to node before left
    for _ in range(left - 1):
        if prev.next is None:
            return
        prev = prev.next

    current = prev.next

    for _ in range(right - left):
        if current is None or current.next is None:
            break

        temp = current.next
        current.next = temp.next
        temp.next = prev.next
        prev.next = temp

    self.head = dummy.next
            
ll = LinkedList()
ll.insert(42)
ll.insert(52)
ll.insert(62)
ll.insert(72)
ll.display()
ll.remove_nth_from_end(2)
ll.display()
ll.reverse_between(2,4)
ll.display()