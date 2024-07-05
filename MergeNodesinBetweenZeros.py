# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        curr=head.next
        s=0
        # l=[]
        while curr is not None:
            if curr.val == 0:
                res=res.next
                res.val=s
                # l.append(s)
                s=0
            else:
                s+=curr.val
            curr=curr.next
        res.next=None
        return head.next
        # dummy=ListNode(0)
        # curr=dummy
        # for i in l:
        #     dummy.next=ListNode(i)
        #     dummy=dummy.next
        # return curr.next
