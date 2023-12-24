class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        sum_list = []
        for account in accounts:
            out = sum(account)
            sum_list.append(out)
        return max(sum_list)



accounts = [[1,2,8],[3,2,1]]
print(Solution().maximumWealth(accounts))

# shorter
#return max(sum(account) for account in accounts)