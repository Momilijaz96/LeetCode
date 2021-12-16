import numpy as np
class Solution:
    def reverse(self, x: int) -> int:
        neg_flag=False
        s=list(str(x))
        if s[0]=='-':
            s.remove('-')
            neg_flag=True
            
        for idx in range(len(s)//2):
            temp=s[idx]
            s[idx]=s[-1*(idx+1)]
            s[-1*(idx+1)]=temp
        
        rev_x=''.join(list(s))
        if neg_flag:
            rev_x='-'+rev_x
            print(rev_x)

        if int(rev_x)>= -2147483648 and int(rev_x)<=2147483647:
            return np.int32(rev_x)
        else: 
            return 0