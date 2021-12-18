from Node import Node

def gen_carry(num):
    if num>9:
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


                
