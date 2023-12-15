class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        numb = int(''.join(map(str, nums)))
        numb = numb + 1
        output = list(map(int, str(numb)))
        return output

nums = [9]
sol_inst = Solution()
answer = sol_inst.plusOne(nums)
print(answer)
        