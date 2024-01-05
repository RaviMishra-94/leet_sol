class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        l = 0
        n = 0
        sub_list = []
        count_list = []
        for start in range(len(nums)):
            for end in range(start + 1, len(nums) + 1):
                subarray = nums[start:end]
                sub_list.append(subarray)

        for items in (sub_list):
            sub_list_sum = len(set(items))
            count_list.append(sub_list_sum)      

        result = [x**2 for x in count_list] 
        return sum(result)
   
        
nums = [1,2,1]
print(Solution().sumCounts(nums))