
class Solution:
    def romanToInt(self, s: str) -> int:
        ro_nu = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        for index, character in enumerate(s) :
             value = ro_nu[character]

             if index == 0 and character == 'I':
                answer = index
             elif index == 1 and character == 'I' :
                 answer += value

             elif index == 2 and character == 'I' :
                 answer += value

             if 0 < index < 2 and character == 'V':
                 answer = ro_nu['V'] 

             elif 0 < index < 2 and character == 'X':
                 answer = ro_nu['I'] 

             
        print(answer)           
                      
solution_instance = Solution()
solution_instance.romanToInt("IV")

