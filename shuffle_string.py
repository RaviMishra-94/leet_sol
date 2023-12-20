class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        s_list = []
        sort_indices = sorted(indices)
        for word in s:
            s_list.append(word)
        
        char_index = sorted(zip(indices, s_list))
        result = ''.join(char for _, char in char_index)
        return result


    






s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
ans = Solution().restoreString(s, indices)