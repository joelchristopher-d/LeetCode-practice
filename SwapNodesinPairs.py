# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curr = head
        head = curr.next       
        if curr.next is not None:          
            while curr.next is not None:
                temp = curr.next.next
                nex = curr
                curr.val,curr.next.val = curr.next.val, curr.val
                curr.next = nex
                curr.next.next = temp
                curr = curr.next
            return head
        return head


