class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        start, end = 1, x
        while start <= end:
            mid = (start + end) // 2
            mid_squared = mid * mid

            if mid_squared == x:
                return mid
            elif mid_squared < x:
                start = mid + 1
                answer = mid
            else:
                end = mid - 1

        return answer
sol_inst = Solution()
answer = sol_inst.mySqrt(8)
print(answer)