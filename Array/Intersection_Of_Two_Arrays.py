class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cmn=[]
        for n1 in nums1:
            if n1 in nums2:
                cmn.append(n1)
                nums2.pop(nums2.index(n1))
        return cmn