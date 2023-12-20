class Solution:
    def finalString(self, s: str) -> str:
        char_to_omit = 'i'
        count_of_i = s.count(char_to_omit)

        for _ in range(count_of_i):
            index_of_i = s.index(char_to_omit)
            first_part = s[:index_of_i] 
            second_part = s[index_of_i+1:] 
            s = first_part[::-1] + second_part

        return s

s = "poiinter"
print(Solution().finalString(s))
