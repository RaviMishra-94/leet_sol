class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        uppercase_dict = {chr(65 + i): i for i in range(26)}
        dic_list = list(uppercase_dict.keys())
        output = ''
        while columnNumber > 0:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            output = dic_list[remainder] + output

        return output
    
columnNumber = 1
sol_inst = Solution()
answer = sol_inst.convertToTitle(columnNumber)
print(answer)
