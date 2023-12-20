class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        import re
        value = 0

        for letter in jewels:
            for i, l in enumerate(letter):
                p1 = re.compile(re.escape(letter[i]))
                for stone in stones:
                    for i, s in enumerate(stone):
                        match = len(p1.findall(stone[i]))
                        value = value + match
            return value
                        
     

jewels = "aA", 
stones = "aAAbbbb"
ans = Solution().numJewelsInStones(jewels, stones)
print(ans)