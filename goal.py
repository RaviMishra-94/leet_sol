class Solution:
    def interpret(self, command: str) -> str:
        inter = command.replace("()", "o").replace("(al)", "al")
        return inter


command = "(al)G(al)()()G"
ans = Solution().interpret(command)
print(ans)