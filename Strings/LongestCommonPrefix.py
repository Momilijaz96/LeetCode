import numpy as np
class Solution:
    def CompareFirst(self, strs, loc):
        count={}
        index={}
        for si,s in enumerate(strs):
            if len(s)>loc:
                if s[loc] in count:
                    count[s[loc]]+=1
                    index[s[loc]].append(si)
                else:
                    count[s[loc]]=1
                    index[s[loc]]=[si]
            else:
                return [],''
        s=strs[0][loc]
        if count[s]==len(strs):
            return index[s],s
        else:
            return [],''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs=np.array(strs)
        if len(strs)>1:
            idx,ch=self.CompareFirst(strs,0)
            loc=1
            prefix=[]
            while(len(idx)>1):
                prefix.append(ch)
                idx,ch=self.CompareFirst(strs[idx],loc)
                loc+=1
            return ''.join(prefix)
        else:
            return strs[0]