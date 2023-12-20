class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        import re
        m_list = []

        pattern = re.compile(rf'{x}+')
        for i, word in enumerate(words):
            match = pattern.findall(word)
            m_list.append(match)
            
        non_empty = [index for index, sublist in enumerate(m_list) if sublist]
        return non_empty
        


words = ["abc","bcd","aaaa","cbc"]
x = "a"    
answer = Solution().findWordsContaining(words, x)
print(answer)