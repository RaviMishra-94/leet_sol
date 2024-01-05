class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        out = [x for x in nums if x != val]
        nums[:] = out  
        return len(out)





nums = [3,4,4,3]
val = 3
print(Solution().removeElement(nums, val))
        