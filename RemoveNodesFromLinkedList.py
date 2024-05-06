# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current:
            runner = current.next
            remove_current = False
            
            while runner:
                if runner.val > current.val:
                    remove_current = True
                    break
                runner = runner.next
            
            if remove_current:
                prev.next = current.next
            else:
                prev = current
            
            current = current.next
        
        return dummy.next
