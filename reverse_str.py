class Solution:
    def reverseWords(self, s: str) -> str:
        rev_list = []
        
        s_split = s.split() 
        for word in s_split:
            output = word[::-1]
            rev_list.append(output)
        fin_lst = ' '.join(rev_list)
        return fin_lst





s = "Let's take LeetCode contest"
answer = Solution().reverseWords(s)
print(answer)
