def swapValues(a,b):
    temp=a
    a=b
    b=temp
    return a,b

def Partition(head,k):
    #Space and Time: O(1) and O(n)
    if k<0 or head==None: #Edge case or error
        return -1
    node=head
    tail=None
    #Get access to tail node
    while(node!=None):
        if node.next==None:
            tail=node
            break
        node=node.next
    #Swap <K nodes with head and >=k with tail
    node=head
    while(node.next!=None):
        if (node.next.val<k):
            head.val,node.next.val=swapValues(head.val,node.next.val)
        elif (node.next.val>=k):
            tail.val,node.next.val=swapValues(tail.val,node.next.val)
        node=node.next
    return head