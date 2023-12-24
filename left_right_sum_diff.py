class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        left_sum = 0
        right_sum = 0
        left_sum_list = [0,]
        right_sum_list = [0,]  
        out_list = []
    
        for num in nums:
            left_sum += num
            left_sum_list.append(left_sum)
        for num in nums[::-1]:
            right_sum += num
            right_sum_list.append(right_sum)              
        
        left_sum_list = left_sum_list[:-1]
        right_sum_list = right_sum_list[:-1]
        right_sum_list = right_sum_list[::-1]

        for i in range(len(nums)):
            out = left_sum_list[i] - right_sum_list[i]
            out_list.append(abs(out))
        return out_list
        

nums = [10,4,8,3]
print(Solution().leftRightDifference(nums))