class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        count = 0
        set_allowed = set(allowed)
        for word in words:
            if set(word).issubset(set_allowed):
                count += 1
        return count
        


allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
ans = Solution().countConsistentStrings(allowed, words)
print(ans) 