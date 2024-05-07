# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val == 0:
            return head
        a=0
        curr = head
        while(curr):
            a=(a*10)+curr.val
            curr=curr.next
        a=a*2
        digits = []
        # return head
        while a:
            t = a % 10
            a //= 10
            digits.append(t)

        digits.reverse()
        head=ListNode()
        curr=head
        for i in digits:
            curr.next=ListNode(i)
            curr=curr.next
        return head.next






# if head.val > 4:
#             head = ListNode(0, head)
#         node = head
#         while node:
#             node.val = (node.val * 2) % 10
#             if node.next and node.next.val > 4:
#                 node.val += 1
#             node = node.next
#         return head
