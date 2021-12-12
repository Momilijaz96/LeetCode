class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        #Check if string has non-alnum characters remove them
        if not s.isalnum():
            s=list(s)
            s_new=[]
            for c in s: #Never make changes on the object on which you are iterating
                if c.isalnum():
                    s_new.append(c)
            s=s_new
        
        #Check if it is a palindrome
        for idx in range(len(s)//2):
            if s[idx]!=s[-1*(idx+1)]:
                return False
            
        return True
            
        