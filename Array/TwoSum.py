class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx,n in enumerate(nums):
            elem = target-n
            #Each element can be used only once, dont self comapre
            if (elem in nums) and (idx!=nums.index(elem)):
                return [idx,nums.index(elem)]
        return []