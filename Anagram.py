class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sc_count={}
        tc_count={}
        for sc,tc in zip(s,t):
            if sc in sc_count:
                sc_count[sc]+=1
            else:
                sc_count[sc]=1
            if tc in tc_count:
                tc_count[tc]+=1
            else:
                tc_count[tc]=1
        for k in sc_count:
            if k not in tc_count or sc_count[k]!=tc_count[k]:
                return False
        return True