from Node import Node

def gen_carry(num):
    res=num%10
    carry=num//10
    return res,carry

def SumLists(h1,h2):
    p1=h1
    p2=h2
    sh=None
    sum=sh
    carry=0
    #Check input for null
    if h1==None or h2==None:
        return -1
    #Compute lists sum
    while(p1!=None or p2!=None):
        if (p1!=None and p2!=None):
            res=p1.data+p2.data+carry
            res,carry=gen_carry(res)
        elif (p1==None):
            res=p2.data+carry
            res,carry=gen_carry(res)
        elif (p2==None):
            res=p1.data+carry
            res,carry=gen_carry(res)
        sum=Node(res)
        sum=sum.next
        p1=p1.next
        p2=p2.next
    #Check if carry is non zero
    if carry>0:
        sum=Node(carry)
    return sh

def SumList_recur(h1,h2):
    return addlist(h1,h2,0)

def addlist(n1,n2,c):
    
    #Base Case
    if (n1==None and n2==None and c==0):
        return None
    #Recursive case
    else: 
        sum=Node()
        v1=n1.data if n1!=None else 0
        v2=n2.data if n2!=None else 0
        sum.data,c=gen_carry(v1+v2+c)
        rem=addlist(None if n1==None else n1.next,
                None if n2==None else n2.next,c)
        sum.next=rem
    return sum

