class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        count = 0
        for i,v  in enumerate(nums):
            for j, value in enumerate(nums):
                if 0 <= i < j < len(nums):
                    if nums[i] + nums[j] < target:
                        count += 1
        return count


nums = [-1,1,2,3,1]
target = 2
print(Solution().countPairs(nums, target))