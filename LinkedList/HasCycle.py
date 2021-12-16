# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if isinstance(head,ListNode):
            v='visited'
            node=head
            while(node.val!=v):
                if (node.next==None):
                    return False
                else:
                    node.val=v
                    node=node.next
            return True
        else:
            return False