class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        return sorted(s) == sorted(t)
        
s = "anagram"
t = "nagaram"
sol_inst = Solution()
ans = sol_inst.isAnagram(s, t)
print(ans)