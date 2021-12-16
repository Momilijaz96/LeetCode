class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for num in nums: #Main loop for picking each num for comparison
            nums.pop(nums.index(num))  #pop the first index where num occurs
            if num in nums: #if we find second occurance of num in nums, we got a duplicate
                return True
        return False
        