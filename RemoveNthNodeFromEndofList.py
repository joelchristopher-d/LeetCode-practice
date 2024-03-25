# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0,head)
        low = high = temp
        for _ in range(n):
            if high.val == None:
                return head
            high = high.next
        
        while(high.next is not None):
            low = low.next
            high = high.next
        low.next = low.next.next
        return temp.next

