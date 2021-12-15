# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if isinstance(head,ListNode):
            #Collect all node values in a list
            values=[]
            values.append(head.val)
            node=head
            while(node.next!=None):
                node=node.next
                values.append(node.val)
            #Check if values are a palindrome
            for i in range(len(values)):
                rev_idx=len(values)-(i+1)
                if values[i]!=values[rev_idx]:
                    return False
            return True
        else:
            return False