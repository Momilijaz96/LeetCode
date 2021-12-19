def IsPalindrome(h):
    #Check input
    if h==None or h.next==None:
        return True
    #Make desired pointers
    a=h
    b=h.next
    fast=h.next.next
    res,ptr=rec_pal(a,b,fast)

def rec_pal(a,b,fast):
    #Base case for odd sized lst
    if (a.data==b.data) and (fast.next==None):
        return True, b.next
    #Base case for even sized list
    elif (a.data==b.next.data) and (fast==None):
        return True,b.next.next
    #Recursive case
    else:
        res,pos=rec_pal(a.next,b.next,fast.next.next)
        if res:
            if a.data==pos.data:
                return True,pos.next
        else:
            return False,None