#Merge 2 Linked List
"""
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
        
def mergeTwoLists(list1,list2):
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next,list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1,list2.next)
        return list2
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

merged = mergeTwoLists(list1, list2)

current = merged
while current:
    print(current.val, end=" -> " if current.next else "")
    current = current.next
"""

#Remove Duplicates from Sorted Linked List
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head
"""

#Partition list
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def partition(head, x):
    beforeHead = ListNode(0)
    afterHead = ListNode(0)
    before = beforeHead
    after = afterHead
    current = head
    while current:
        nextNode = current.next   
        current.next = None       
        if current.val < x:
            before.next = current
            before = before.next
        else:
            after.next = current
            after = after.next
        current = nextNode
    before.next = afterHead.next
    return beforeHead.next
"""

#Merge K sorted Lists
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next

def mergeKLists(lists):
    if not lists:
        return None
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(mergeTwoLists(l1, l2))
        lists = merged
    return lists[0]
"""