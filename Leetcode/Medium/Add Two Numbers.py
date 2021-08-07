# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.l1=l1
        self.l2=l2
        summ=self.l1.val + self.l2.val
        carry=int(summ/10)
        l3=ListNode(summ%10)
        p1=self.l1.next
        p2=self.l2.next
        p3=l3
        while(p1!=None or p2!=None):
            summ=carry+(p1.val if p1 else 0)+(p2.val if p2 else 0)
            carry=int(summ/10)
            p3.next=ListNode(summ%10)
            p3=p3.next
            p1=p1.next if p1 else None
            p2=p2.next if p2 else None
        if(carry>0):
            p3.next=ListNode(carry)
        return l3
