class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        max_nums = max(nums)
        result = 0
        while k:
            result += max_nums
            max_nums += 1  
            k -= 1
        return result


nums = [4,4,9,10,10,9,3,8,4,2,5,3,8,6,1,10,4,5,3,2,3,9,5,7,10,4,9,10,1,10,4]
k = 6
print(Solution().maximizeSum(nums, k))