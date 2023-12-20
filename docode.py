class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # Create a dictionary mapping each letter in the key to the corresponding letter in the alphabet
        key_dict = {key[index]: chr(index + ord('a')) for index in range(len(key))}

        # Decode the message
        decoded_message = ''.join(key_dict.get(word, word) for word in message.split())

        return decoded_message

# Example usage
key = "thequickbrownfoxjumpsoverthelazydog"
message = "vkbs bs t suepuv"
ans = Solution().decodeMessage(key, message)
print(ans)
