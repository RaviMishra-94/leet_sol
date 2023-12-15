from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        major = n // 2
        count_dict = []

        cound = dict(Counter(nums))
        count_dict.append(cound)       
        for k, v in count_dict:
            if major > v:
                return k


nums = [2,2,1,1,1,2,2]
sol_inst = Solution()
answer = sol_inst.majorityElement(nums)
print(answer)