class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if not char in magazine:
                return False
            magazine = magazine.replace(char, "", 1)
        return True