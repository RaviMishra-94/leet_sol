class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        even_index = []
        odd_index = []
        for i, v in enumerate(nums):
            if i % 2 == 0:
                even_index.append(v)
            else:
                odd_index.append(v)
        result_list = [item2 for item1, item2 in zip(even_index, odd_index) for _ in range(item1)]
        return result_list

        



nums = [2,3,4,5,6,7]
print(Solution().decompressRLElist(nums))
        