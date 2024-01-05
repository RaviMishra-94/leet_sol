class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        output_list = []

        for i, v in enumerate(nums):
            output_list.insert(index[i], v)
        return output_list



nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
print(Solution().createTargetArray(nums, index))
