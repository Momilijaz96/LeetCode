class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        for idx in range(len(s)//2):
            temp=s[idx]
            s[idx]=s[-1 * (idx+1)]
            s[-1 * (idx+1)] = temp
            