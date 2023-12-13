class Solution:
    def romanToInt(self, s: str) -> int:
        ro_nu = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        for i in range(len(s)):
            if i < len(s) - 1 and ro_nu[s[i]] < ro_nu[s[i + 1]]:
                result -= ro_nu[s[i]]
            else:
                result += ro_nu[s[i]]

        return result

# Example usage:
solution_instance = Solution()
print(solution_instance.romanToInt("IV"))
