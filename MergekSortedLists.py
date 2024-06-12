# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l=[]
        for i in lists:
            j=i
            while(j is not None):
                l.append(j.val)
                j=j.next
        l.sort()
        n=ListNode(0)
        dummy=n
        for i in l:
            new = ListNode(i)
            dummy.next=new
            dummy=dummy.next
        return n.next
        
