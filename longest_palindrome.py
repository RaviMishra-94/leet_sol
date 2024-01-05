class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal_list = []
        s = list(s)
        s_len = len(s)

        if s_len % 2 != 0:
            middle_index = int(s_len / 2 - 0.5)
            left = 0
            right = s_len - 1
            while left != middle_index:               
                if s[left] == s[right]:
                    pal_list.append(s[left])
                    pal_list.append(s[middle_index])
                    pal_list.append(s[right])                   
                    left += 1
                    right -= 1
                    
                else:
                    left += 1
                    right -= 1

        elif s_len % 2 == 0:
            left = int(s_len / 2 - 1)
            right = int(s_len / 2)
            while left >= 0 or right < s_len:
                if s[left] == s[right]:
                    pal_list.append(s[left])
                    pal_list.append(s[right]) 
                    left -= 1
                    right += 1
                else:
                    left -= 1
                    right += 1
        


        if len(pal_list) == 0:
            pal_list = s[0]
            
        return ''.join(pal_list)


s = "adam"
print(Solution().longestPalindrome(s))