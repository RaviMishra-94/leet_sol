class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sums_list = []
        sum_nums = 0
        for i in range(len(nums)):
            sum_nums = sum_nums + nums[i]
            sums_list.append(sum_nums)
        return sums_list

nums = [1,2,3,4]
print(Solution().runningSum(nums))