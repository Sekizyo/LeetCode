class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for char in s:
            if not char.isalnum():
                s = s.replace(char, "")

        splited = list(s)
        splited.reverse()
        for i, char in enumerate(s):
            if char != splited[i]:
                return False
            
        return True