class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed([w for w in s.split(" ") if len(w) > 0]))
