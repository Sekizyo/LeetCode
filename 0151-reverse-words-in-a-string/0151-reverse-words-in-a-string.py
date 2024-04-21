class Solution:
    def reverseWords(self, s: str) -> str:
        splited = s.split()
        splited.reverse()
        return ' '.join(splited)