class Solution:
    def reverse(self, x: int) -> int:
        # Define the upper and lower bounds for a 32-bit signed integer
        INT32_MIN, INT32_MAX = -2**31, 2**31 - 1

        # Convert the integer to a string
        x_str = str(x)

        # Check if the number is negative
        if x_str[0] == '-':
            reversed_str = '-' + x_str[:0:-1]
        else:
            reversed_str = x_str[::-1]

        # Convert the reversed string back to an integer
        reversed_x = int(reversed_str)

        # Check for overflow
        if reversed_x < INT32_MIN or reversed_x > INT32_MAX:
            return 0

        return reversed_x


x = 123
print(Solution().reverse(x))
