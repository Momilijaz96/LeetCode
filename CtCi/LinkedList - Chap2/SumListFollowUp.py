from Node import Node

def gen_carry(num):
    res=num%10
    carry=num//10
    return res,carry

def SumLists2(h1,h2):
    #Compute list sizes
    n1=h1
    n2=h2
    len1=0
    len2=0
    while(n1!=None or n2!=None):
        if(n1!=None):
            len1+=1
            n1=n1.next
        if(n2!=None):
            len2+=1
            n2=n2.next
    
    #Append shorter list with zero nodes
    if len1!=len2:
        long_list,short_list=h2,h1 if len1<len2 else h1,h2
        diff=abs(len1-len2)
        count=0
        while(count<diff):
            node=Node(0)
            node.next=short_list
            short_list=node
            count+=1
            return addlist2(short_list,long_list)
    else:
        return addlist2(h1,h2)

def addlist2(n1,n2):
    
    #Base case
    if (n1==None and n2==None):
        return None,0
    else: #Recursive case
        sum=Node()
        rem,prev_carry=addlist2(None if n1==None else n1.next,
                                None if n2==None else n2.next)
        v1=0 if n1==None else n1.data
        v2=0 if n2==None else n2.data
        sum.data,next_carry=gen_carry(v1+v2+prev_carry)
        sum.next=rem
        return sum,next_carry


