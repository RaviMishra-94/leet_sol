class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        result_list = []
        gain.insert(0, 0)
        n = len(gain)
        for i in range(n):
            out = sum(gain[:i+1]) - gain[0]
            result_list.append(out)
        return max(result_list)








gain = [-5,1,5,0,-7]
print(Solution().largestAltitude(gain))