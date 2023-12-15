class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Merge nums1 and nums2 and sort the result
        nums1[:m + n] = sorted(nums1[:m] + nums2)
        print(nums1)

# Test case
nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
m = 6
nums2 = [1, 2, 2]
n = 3

sol_inst = Solution()
sol_inst.merge(nums1, m, nums2, n)