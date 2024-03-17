# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1str = ""
        l2str = ""
        currentl1 = l1
        currentl2 = l2

        while (currentl1!=None):
            l1str=str(currentl1.val)+l1str
            currentl1 = currentl1.next
            
        while(currentl2!=None):
            l2str=str(currentl2.val)+l2str
            currentl2 = currentl2.next

        total = int(l1str)+int(l2str)
        l3=ListNode()
        current = l3
        if total==0:
            l3.next = ListNode(0)

        while total:
            current.next=(ListNode(total%10))
            total//=10
            current=current.next
        
        return l3.next
        

        
        
