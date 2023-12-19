class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        import re

        plus_pattern1 =  re.compile(r'X\++|\++X')
        minus_pattern1 = re.compile(r'\--X|X\--')
        
        rp1 = len([operation for operation in operations if plus_pattern1.search(operation)])
        rm1 = - len([operation for operation in operations if minus_pattern1.search(operation)])
        
        result = rp1  + rm1 
        return result
    
operations = ["++X","++X","X++"]
ans = Solution().finalValueAfterOperations(operations)
print(ans)