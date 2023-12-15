class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        uppercase_dict = {chr(65 + i): i + 1 for i in range(26)}

        result = 0
        for char in columnTitle:
            result = result * 26 + uppercase_dict[char]

        return result

columnTitle = "ABCDEFG"
sol_inst = Solution()
answer = sol_inst.titleToNumber(columnTitle)
print(answer)
