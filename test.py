class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        import re

        plus_pattern1 =  re.compile(r'X\++|\++X')
        minus_pattern1 = re.compile(r'\--X|X\--')
        

        result_plus1 = [plus_pattern1.findall(operation) for operation in operations]
        result_minus1 = [minus_pattern1.findall(operation) for operation in operations]


        fp1 = [inner_list for inner_list in result_plus1 if inner_list]
        fm1 = [inner_list for inner_list in result_minus1 if inner_list]
    
     
        rp1 = len(fp1)
        rm1 = - len(fm1)
        
        result = rp1  + rm1 
        return result
    
operations = ["++X","++X","X++"]
ans = Solution().finalValueAfterOperations(operations)
print(ans)