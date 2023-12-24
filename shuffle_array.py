class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        new_nums = []
        first_nums = nums[:n]
        second_half = nums[n:] 
        for i in range(n):
            new_nums.append((first_nums[i], second_half[i]))
        flat_list = [item for tuple_pair in new_nums for item in tuple_pair]
        return flat_list

nums = [2,5,1,3,4,7]
n = 3
print(Solution().shuffle(nums, n))
        