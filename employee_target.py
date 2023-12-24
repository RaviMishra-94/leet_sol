class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        hour_list = []
        for hour in hours:
            if hour >= target:
                hour_list.append(hour)
            else:pass
        return len(hour_list)

hours = [0,1,2,3,4]
target = 2
print(Solution().numberOfEmployeesWhoMetTarget(hours, target))