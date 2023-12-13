class Solution:
    def mergeTwoLists(self, list1 , list2):
      output = []
      for n in list1:
        output.append(n)
      for m in list2:
        output.append(m)
      print(sorted(output)) 

list1 = [1,2,4]
list2 = [1,3,4]

sol = Solution()
result = sol.mergeTwoLists(list1, list2)
print(result)