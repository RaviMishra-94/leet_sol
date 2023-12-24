class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        output = nums + nums
        return output



nums = [1,2,1]
print(Solution().getConcatenation(nums))