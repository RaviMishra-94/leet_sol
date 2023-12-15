class Solution:
    def singleNumber(self, nums: list[int]) -> int:
      
        result = 0
        for num in nums:
            result ^= num
        return result

nums = [4,1,2,1,2]
sol_inst = Solution()
answer = sol_inst.singleNumber(nums)
print(answer)