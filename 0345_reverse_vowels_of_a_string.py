class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        vowels_in_s = []

        for i in range(len(s)):
            if s[i] in vowels:
                vowels_in_s.append(s[i])

        result = ""
        for i in range(len(s)):
            if s[i] in vowels:
                result += vowels_in_s.pop()
            else:
                result += s[i]

        return result
