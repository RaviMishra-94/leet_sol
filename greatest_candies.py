class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies_list= []

        for candy in candies:
            if candy + extraCandies >= max(candies):
                output = True 
                max_candies_list.append(output)        
            else: 
                output = False
                max_candies_list.append(output)
        
        return max_candies_list

        
candies = [2,3,5,1,3]
extraCandies = 3
print(Solution().kidsWithCandies(candies, extraCandies))