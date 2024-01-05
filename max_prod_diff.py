class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        prod_list = []
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i != j:
                    out = nums[i] * nums[j]
                    prod_list.append(out)
        return max(prod_list) - min(prod_list)





nums = [5,6,2,7,4]
print(Solution().maxProductDifference(nums))