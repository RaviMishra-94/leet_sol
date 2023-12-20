class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        key_to_index = {'type': 0, 'color': 1, 'name': 2}
        valv = key_to_index.get(ruleKey, -1)  # Default to -1 if ruleKey is not in the dictionary

        coun = []
        enum_list = [{'index': index, 'item': item} for index, item in enumerate(items)]

        indexed_list = [{'index': outer['index'], 'nested_index': inner_index, 'value': value}
                        for outer in enum_list
                        for inner_index, value in enumerate(outer['item'])]

        for item in indexed_list:
            if item['nested_index'] == valv and item['value'] == ruleValue:
                output = 1
                coun.append(output)

        return sum(coun)

items = [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]]
ruleKey = "type"
ruleValue = "phone"
answer = Solution().countMatches(items, ruleKey, ruleValue)
print(answer)
