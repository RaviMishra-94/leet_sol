class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        try:
            max_nums = max(nums)
            max_values = [value for value in nums if value == max_nums]
            second_max = max([num for num in nums if num != max_nums])
            if len(max_values) > 1:
                output = (max(max_values) - 1 ) ** 2
            else:
                output = (max(nums) - 1) * (second_max - 1)
        except ValueError:
            output = 0 
        return output



nums = [1,1,1,1]
print(Solution().maxProduct(nums))