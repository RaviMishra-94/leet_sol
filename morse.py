class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_code_table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        def word_to_morse(word):
            return ''.join(morse_code_table[ord(char) - ord('a')] for char in word)

        unique_morse_set = set()

        for word in words:
            morse_representation = word_to_morse(word)
            unique_morse_set.add(morse_representation)

        return len(unique_morse_set)

words = ["gin","zen","gig","msg"]
ans = Solution().uniqueMorseRepresentations(words)
print(ans)
