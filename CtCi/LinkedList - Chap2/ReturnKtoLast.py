def RemoveKtoLast(head,k):
    #Solution3 - with 2 pointers k nodes apart
    p1=head
    #Set p2 k nodes ahead of p1
    node=head
    count=0
    while(node.next!=None):
        if count==k:
            p2=node
            break
        node=node.next
        count+=1
    
    #Check if p2 exits, otherwise k was bigger than list size
    if p2 not in locals():
        return -1
    
    #Traverse through list to return kth last
    while(p2!=None):
        p2=p2.next
        p1=p1.next
    
    return p1

def RemoveKtoLast_recur(node,k):
    if node==None:
        return 0
    else:
        idx=RemoveKtoLast_recur(node.next,k)+1
        if idx==k:
            return node
        return idx