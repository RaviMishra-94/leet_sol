class Solution:
    def defangIPaddr(self, address: str) -> str:
        import re
        return re.sub(r'\.', r'[.]', address)
    
      





address = "1.1.1.1"
ans = Solution().defangIPaddr(address)
print(ans)