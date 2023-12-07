class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(f"Index{i} = {nums[i]}")
                    print(f"Index{j} = {nums[j]}")

nums = range(0, 9)
target = 9
Solution().twoSum(nums, target)