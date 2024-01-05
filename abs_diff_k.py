class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        diff_list = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    diff_list.append(1)

        return sum(diff_list)

nums = [3, 2, 1, 5, 4]
k = 2
print(Solution().countKDifference(nums, k))
