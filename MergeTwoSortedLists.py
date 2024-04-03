# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        def merge(head1,head2):
            if head1 is None:
                return head2
            elif head2 is None:
                return head1
            else:
                if head1.val<=head2.val:
                    temp = head1
                    temp.next=merge(head1.next,head2)
                else:
                    temp = head2
                    temp.next = merge(head1,head2.next)
                return temp

        return merge(list1,list2)


