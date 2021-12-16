# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if isinstance(head,ListNode): #Always check input types
            values=[]
            node=head
            values.append(head.val)
            while(node.next!=None):
                values.append(node.next.val)
                node=node.next
            node=head
            for i in range(1,len(values)+1):
                i=i*-1
                node.val=values[i]
                node=node.next
            return head
        else:
            return head