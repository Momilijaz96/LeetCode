# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getNfromStart(self, head, n):
        node=head
        list_size=1
        while(node.next!=None):
            node=node.next
            list_size+=1
        return list_size-(n-1)
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_idx=1
        n=self.getNfromStart(head,n)
        print("New index: ",n)
        if n==node_idx:
            return head.next
        node=head
        while(node.next!=None):
            if node_idx==n-1:
                node.next=node.next.next
                break
            node=node.next
            node_idx+=1
        return head