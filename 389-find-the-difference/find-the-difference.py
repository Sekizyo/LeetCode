class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i, letter in enumerate(s):
            if letter != t[i]:
                return t[i]
        return t[-1]
        