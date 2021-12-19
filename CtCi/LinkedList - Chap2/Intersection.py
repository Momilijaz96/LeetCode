def getLenAndTail(n1,n2):
    l1=1
    l2=2
    while(n1.next!=None or n2.next!=None):
        if(n1.next!=None):
            l1+=1
            n1=n1.next
        else:
            tail1=n1
        
        if(n2.next!=None):
            l2+=1
            n2=n2.next
        else:
            tail2=n2
    return l1,tail1,l2,tail2

def Intersect(h1,h2):
    n1=h1
    n2=h2
    #Set pointers
    l1,tail1,l2,tail2=getLenAndTail(n1,n2)
    s,l=n2,n1 if l2<l1 else n1,n2
    for i in range(abs(l1-l2)):
        l=l.next
    #Check if intersection is there
    intersect=False
    if tail1==tail2:
        intersect=True
    
    #Find merge point
    if intersect:
        while(s!=None or l!=None):
            if s.next==l.next:
                inode=s.next
                return True,intersect
            l=l.next
            s=s.next
    else:
        return False,None        
    

    