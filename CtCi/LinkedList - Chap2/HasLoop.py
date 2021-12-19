def ismarked(n):
    return n.data==-1

def HasLoop(h):
    if h==None:
        return False
    elif h.next==h:
        return True
    n=h
    while(not ismarked(n)):
        n.data=-1
        if(n.next==None):
            return False,None
        n=n.next
    return True,n
