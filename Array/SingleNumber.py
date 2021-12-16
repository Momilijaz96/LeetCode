class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num in set(nums):
            nums.pop(nums.index(num)) #Remove first occurance of num
            try:
                nums.pop(nums.index(num)) #Try removing it again
            except:
                return num #if we get error, there was no second occurance of num, its our single num