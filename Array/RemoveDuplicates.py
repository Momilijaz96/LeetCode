#PROBLEM STATEMENT

"""
Remove duplicates from an ascending sorted list of numbers,
and put the unique numbes in the top k positions of sam elist,
where k is number of unique elements.

"""

#Solution
class Solution:
	def __init__(self,nums):
		self.nums=nums

	def removeDuplicates(self):
		if len(self.nums)>0:
			unique=[]
			#Find unique elements duplicates
			for i in range(len(self.nums)-1):
			    if self.nums[i]!=self.nums[i+1]:
			        unique.append(self.nums[i])
			#Last number is not compares so always uique
			unique.append(self.nums[-1])
			self.nums[:len(unique)]=unique
			return len(unique)
		else:
			return 0

#Main Program
nums=(input("Please enter nums array (comma seperated w/o brackets): ")).split(',')
sol=Solution(nums)

print("Unique Numbers: ",sol.removeDuplicates())
print("Updated nums: ",(sol.nums))