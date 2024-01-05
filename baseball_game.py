class Solution:
    def calPoints(self, operations: list[str]) -> int:
        new_list = []

        for letter in operations:
            if letter.isdigit() or (letter[0] == '-' and letter[1:].isdigit()):
                new_list.append(int(letter))
            elif letter == "C":
                if new_list:
                    new_list.pop()
            elif letter == "D":
                out = int(new_list[-1]) * 2
                new_list.append(out)
            elif letter == "+":
                out = int(new_list[-1]) + int(new_list[-2])
                new_list.append(out)

        return sum(new_list)

operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]
print(Solution().calPoints(operations))
