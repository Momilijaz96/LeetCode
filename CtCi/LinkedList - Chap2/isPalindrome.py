'''
CtCi solutions:
1. reverse the list and compare
2. push first half on stack, then pop and compare with next half
3. recursively :)
'''

def isPalindrome(h):
    #Check input
    if h==None:
        return False
    elif h.next==None:
        return True
    #Extract values and put in a list
    val=[h.data]
    node=h
    while(node.next!=None):
        val.append(node.next.data)
        node=node.next
    #Compare list values to see if its a palindrome
    for i in range(len(val)//2):
        if val[i]!=val[-1(i+1)]:
            return False
    return True
