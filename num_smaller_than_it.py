class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        n = len(nums)
        num_smaller = []
        for i in range(n):
             count_greater = sum(num < nums[i] for num in nums)
             num_smaller.append(count_greater)          
        return num_smaller


nums = [8,1,2,2,3]
print(Solution().smallerNumbersThanCurrent(nums))
        