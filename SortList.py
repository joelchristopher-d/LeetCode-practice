# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        curr=head
        while curr is not None:
            l.append(curr.val)
            curr=curr.next
        dummy = ListNode(0)
        curr=dummy
        for i in sorted(l):
            temp=ListNode(i)
            curr.next=temp
            curr=curr.next
        return dummy.next

        
        
