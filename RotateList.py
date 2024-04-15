# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k==0:
            return head
        count = 1
        curr = head
        prev=None
        while(curr.next is not None):
            count+=1
            prev = curr
            curr=curr.next
        if k==count or k%count == 0:
            return head
        k%=count
        count-=k
        curr=head
        prev=None
        for i in range(count):
            prev=curr
            curr=curr.next
            
        temp=curr
        prev.next=None
        # return head
        while(curr.next is not None):
            curr=curr.next
        curr.next = head
        # prev=None
        # return curr
        head= temp
        return head
            
        
