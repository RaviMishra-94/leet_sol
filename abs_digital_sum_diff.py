class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        num_sum = 0
        digit_sum = 0
        string_nums = str(nums)
        for i in range(len(nums)):
            num_sum += nums[i]
        digits = ''.join(char for char in string_nums if char.isdigit())
        for digit in digits:
            digit_sum += int(digit)
        out = abs(num_sum - digit_sum)
        return out











nums = [1,15,6,3]
print(Solution().differenceOfSum(nums))