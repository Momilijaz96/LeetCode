class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k<len(nums):
            #Roate right is equal to rotate left by len(n)-k steps
            #using this approch to allows inplace assignment, as using =  makes new var
            m=len(nums)-k
        else: 
            #If k>len(n) than right roate by k, wihh produce original array after k%len(n) steps,
            #it is just like rotating array to right by k%len(n) steps, so here roate right is equal to
            #roate left by this exp
            m=len(nums)-(k%len(nums))
        
        for i in range(m):
            nums.append(nums[0])
            nums.pop(0)


nums=[1,2,3,4]
k=5
Solution().rotate(nums,k)
print(nums)
