class Solution:
    def isPalindrome(self, x: int) -> bool:

        x_str = str(x)

        return x_str == x_str[::-1]

# Example usage
sol = Solution()
result = sol.isPalindrome(-121)
print(result)
