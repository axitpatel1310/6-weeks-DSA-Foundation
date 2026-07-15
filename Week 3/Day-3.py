"""
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

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next        
            if slow is fast:
                return True
        return False
    
            
ll = LinkedList()
ll.insert(42)
ll.insert(52)
ll.insert(62)
ll.insert(72)
ll.insert(82)
ll.insert(42)
ll.display()

current = ll.head
while current.next:
    current = current.next
current.next = ll.head.next
print(ll.has_cycle())
"""

#Happy numbers
"""
class Solution:
    def happy_nums(self,num):
        return sum(int(i) ** 2 for i in str(num))
        
sol = Solution()
print(sol.happy_nums(19))
"""

#Find Duplicates 
"""
class Solution:
    def find_dup(self,arr):
        left = 1
        right = len(arr)-1
        while left < right:
            mid = left + (right-left) // 2
            count = 0
            for num in arr:
                if num <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left
    
nums = [1,2,3,4,5,2]
sol = Solution()
print(sol.find_dup(nums))
"""