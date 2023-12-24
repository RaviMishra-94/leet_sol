class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == 0:
            return 0

        if (dividend < 0) != (divisor < 0):
            sign = -1
        else:
            sign = 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        result = sign * quotient

        return min(max(result, INT_MIN), INT_MAX)


dividend = 7
divisor = -3
print(Solution().divide(dividend, divisor))