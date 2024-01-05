class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        total_sum = 0
        
        for start in range(len(arr)):
            for end in range(1, len(arr) - start + 1, 2):
                total_sum += sum(arr[start:start + end])
        
        return total_sum





arr = [1,4,2,5,3]
print(Solution().sumOddLengthSubarrays(arr))