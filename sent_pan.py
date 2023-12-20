class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet_dict = "abcdefghijklmnopqrstuvwxyz"
        dup_remove = ''.join(set(sentence))
        sen_sort = sorted(dup_remove)
        fin_str = ''.join(sen_sort)
        return fin_str == alphabet_dict


sentence = "thequickbrownfoxjumpsoverthelazydog"
ans = Solution().checkIfPangram(sentence)
print(ans)