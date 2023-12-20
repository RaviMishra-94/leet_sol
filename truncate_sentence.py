class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        s_split = s.split()       
        if 0 <= k < len(s_split):
            s_split = s_split[:k]
            s_joint = ' '.join(s_split)
            return s_joint
        else:
            return s




s = "What is the solution to this problem"
k = 4
ans = Solution().truncateSentence(s, k)
print(ans)
