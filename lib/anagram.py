class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word):
        matching_words = []

        for w in word:
            if self.is_anagram(w):
                matching_words.append(w)

        return matching_words

    def is_anagram(self, other_word):
        # Check if the sorted letters of both words are the same
        return sorted(self.word.lower()) == sorted(other_word.lower())

# # Example usage
# anagram_instance = Anagram("enlist")
# result = anagram_instance.match(["listen", "silent", "hippopotamus"])
# print(result)  # Output: ['listen', 'silent']

