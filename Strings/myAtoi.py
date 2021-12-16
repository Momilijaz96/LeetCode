import numpy as np
class Solution:
    def clipInt32(self,s):
        pos_max= 2147483647
        neg_min= -2147483648
        if int(s)>=pos_max:
            return pos_max
        elif int(s)<=neg_min:
            return neg_min
        else:
            return np.int32(s)
    
    def myAtoi(self, s: str) -> int:
        digits=[]
        have_digits=False
        for ch in s:
            if not ch.isdigit():
                if  ch==' ' and (len(digits)==0): #Only leading spaces ignored
                    pass
                elif (ch=='+' or ch=='-') and (len(digits)==0): #Only leading +/- sign taken
                    digits.append(ch)
                else:
                    break
            else:
                digits.append(ch)
                have_digits=True
        if len(digits)>0 and have_digits:
            print(digits)
            digits=''.join(digits)
            return self.clipInt32(digits)
        else:
            return 0
            