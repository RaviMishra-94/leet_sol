class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for index, num in enumerate(nums):
            if num >= target:
                return (int(index))  
            if target not in nums  and target > max(nums):
                output = (len(nums)) 
            else:
                output = 0        
            
        return output  
        
            

nums = [1,3,5,6]
target = 2
print(Solution().searchInsert(nums, target))