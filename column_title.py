class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        uppercase_dict = {chr(65 + i): i + 1 for i in range(26)}

        results = []
        for char in columnTitle:
            result = uppercase_dict[char]
            results.append(result)

        if len(results) == 1:
            return results[0]
        elif len(results) == 2:
            return results[0] * 26 + results[1]
        elif len(results) == 3:
            return results[0] * 26**2 + results[1] * 26 + results[2]
        elif len(results) == 4:
            return results[0] * 26**3 + results[1] * 26**2 + results[2] * 26 + results[3]
        elif len(results) == 5:
            return results[0] * 26**4 + results[1] * 26**3 + results[2] * 26**2 + results[3] * 26 + results[4]
        elif len(results) == 6:
            return results[0] * 26**5 + results[1] * 26**4 + results[2] * 26**3 + results[3] * 26**2 + results[4] * 26 + results[5]
        else: 
            len(results) == 7
            return results[0] * 26**6 + results[1] * 26**5 + results[2] * 26**4 + results[3] * 26**3 + results[4] * 26**2 + results[5] * 26 + results[6]


columnTitle = "ABCDEFG"
sol_inst = Solution()
answer = sol_inst.titleToNumber(columnTitle)
print(answer)
