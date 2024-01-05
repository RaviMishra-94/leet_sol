class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result_list1 = []
        result_list2 = []
    
        for i, v in enumerate(nums1):
            if v in nums2:
                result_list1.append(i)

        for j, v2 in enumerate(nums2):
            if v2 in nums1:
                result_list2.append(j)

        
        if len(result_list1) < 1 or len(result_list2) < 1:
            result = [0, 0]
        else:
            result = [len(result_list1), len(result_list2)]
        return result
    
nums1 = [10,30,16,18]
nums2 = [23,30,30,6,10,26,9,27,6,16,18,10,27,2,20,7,16]
print(Solution().findIntersectionValues(nums1, nums2))