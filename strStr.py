class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        elif (len(haystack)<len(needle)):
            return -1
        
        else:
            ntip=needle[0]
            for hi,ch in enumerate(haystack):
                
                if ch==ntip:
                    print(ch," matched")
                    if haystack[hi:hi+len(needle)]==needle:
                        return hi
                print(ch,"passed")
            return -1
                    