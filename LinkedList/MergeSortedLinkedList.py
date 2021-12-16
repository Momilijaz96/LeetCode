# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #Update ptr in loop
    def updatePtrloop(self,a,b,s):
        if (a.val < b.val):
            s.next=a
            a=a.next
            s=s.next
        elif(b.val < a.val):
            s.next=b
            b=b.next
            s=s.next
        else:
            s.next=a
            a=a.next
            s.next.next=b #Order matters here too, update a first then s
            b=b.next
            s=s.next.next
        return a,b,s
    
    #Update heads
    def updateHead(self,a,b):
        if a.val<b.val:
            mh=a
            s=a
            a=a.next
        elif b.val<a.val:
            mh=b
            s=b
            b=b.next
        else:
            mh=a
            s=a
            a=a.next
            s.next=b #Order matters here, change s.next after moving a, as they point to same node
            b=b.next
            s=s.next
        return a,b,s,mh
    
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        
        if isinstance(a,ListNode) and isinstance(b,ListNode):
            
            a,b,s,mh=self.updateHead(a,b)
            
            while(a!= None and b!= None):
                a,b,s=self.updatePtrloop(a,b,s)
                
            if a==None:
                s.next=b
            elif b==None:
                s.next=a
            return mh
        
        elif isinstance(a,ListNode):
            return a
        else:
            return b
            
