class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        count_list = []
        
        for sentence in sentences:
            space_count = sentence.count(' ')
            count_list.append(space_count)
            
        max_words = max(count_list)
        output = max_words + 1
        return output
    

sentences = ["alice and bob love leetcode","i think so too","this is great thanks very much"]
answer = Solution().mostWordsFound(sentences)
print(answer)