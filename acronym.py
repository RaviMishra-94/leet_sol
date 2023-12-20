class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        first_letter = ''.join([word[0] for word in words])
        return first_letter == s

words = ["alice", "bob", "charlie"]
s = "abc"
print(Solution().isAcronym(words, s))