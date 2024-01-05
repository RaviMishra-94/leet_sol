class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        l = len(nums1)
        if l % 2 != 0:
            middle_index = int(l / 2 - 0.5)
            median = nums1[middle_index]

        else:
            index_left = int(l / 2 - 1) 
            index_right = int(l / 2 )
            median = ((nums1[index_left] + nums1[index_right]) / 2)

        return median








nums1 = [1, 2]
nums2 = [3, 4]

print(Solution().findMedianSortedArrays(nums1, nums2))
        