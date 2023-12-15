
class Solution:
    def climbStairs(self, n: int) -> int:
        output_list = []
        calc_list = []
        for num in range(1, n+1):
            output_list.append(num)
        for index in range(n):
            if index < 2:
                result = output_list[index]
            else:
                result = calc_list[index - 1] + calc_list[index - 2]
            calc_list.append(result)
            output = calc_list[-1]
        return output

        print(output)
    

sol_inst = Solution()
ans = sol_inst.climbStairs(3)

