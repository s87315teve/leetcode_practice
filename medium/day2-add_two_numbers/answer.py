# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1.val+=l2.val
        carry=l1.val//10
        l1.val=l1.val%10
        if carry>0:
            if l1.next==None:
                l1.next=ListNode(0)
            l1.next.val+=carry    
        if l1.next!=None or l2.next!=None:
            if l1.next==None:
                l1.next=ListNode(0)
            if l2.next==None:
                l2.next=ListNode(0)
            l1.next=self.addTwoNumbers(l1.next, l2.next)
        return l1