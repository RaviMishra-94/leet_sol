class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        sub_list = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[i] - nums[j] == diff and nums[j] - nums[k] == diff:
                        sub_list += 1
        return sub_list
        


nums = [4,5,6,7,8,9]
diff = 2
print(Solution().arithmeticTriplets(nums, diff))