class Solution:
    def intToRoman(self, num: int) -> str:
        roman_mapping = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        result = ""

        for value, numeral in roman_mapping:
            count = num // value
            result += numeral * count
            num -= value * count

        return result

# Example usage:
solution_instance = Solution()
print(solution_instance.intToRoman(2))
