class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_1 = ''.join(char for char in s if char.isalnum())
        s_2 = s_1[::-1]

        return s_1 == s_2
          
       



s = "0P"
sol_inst = Solution()
result = sol_inst.isPalindrome(s)
print(result)
