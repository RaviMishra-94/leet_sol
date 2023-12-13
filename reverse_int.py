class Solution:
    def reverse(self, x: int) -> bool:

        x_str = str(x)

        return x_str[::-1]

# Example usage
sol = Solution()
result = sol.reverse(-123)
print(result)
