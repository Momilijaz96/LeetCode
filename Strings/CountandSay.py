class Solution:
    
    def s2w(self,s):
        count=1
        orig_len=len(s)
        s+='0'
        res=[]
        for idx in range(orig_len):
            if s[idx]==s[idx+1]:
                count+=1
            else:
                res.append(str(count)+s[idx])
                count=1
        #if len(res)>1:
        #   res = ''.join(res)
        return ''.join(res)
    
    def countAndSay(self, n: int) -> str:
        seq='1'
        if n==1:
            return seq
        else:
            for i in range(n-1):
                seq=self.s2w(seq)
            return seq