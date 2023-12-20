class Solution:
    def sortSentence(self, s: str) -> str:
        s_split = s.split()
        sorted_words = sorted(s_split, key=lambda x: int(''.join(filter(str.isdigit, x))))
        result_str = ' '.join(sorted_words)
        result_str_split = result_str.split()
        final_list = [word[:-1] for word in result_str_split]   
        final_joint = ' '.join(final_list)
        return final_joint
        

s = "is2 sentence4 This1 a3"
ans = Solution().sortSentence(s)
print(ans)