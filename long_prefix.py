class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        shortest_str = min(strs, key=len)
        for i, char in enumerate(shortest_str):
            if not all(word[i] == char for word in strs):
                return shortest_str[:i]
        return shortest_str

strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))
