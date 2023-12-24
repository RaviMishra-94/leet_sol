class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        good_pair = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    good_pair.append((i,j))
        return len(good_pair)


nums = [1,2,3,1,1,3]
print(Solution().numIdenticalPairs(nums))



