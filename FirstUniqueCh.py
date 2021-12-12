class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count={}
        for c in s:
            if c in count:
                count[c]+=1
            else:
                count[c]=1
                
        first_unique=''
        for key in list(count.keys()):     
            if count[key]==1:
                first_unique=key
                return s.index(key)
        return -1