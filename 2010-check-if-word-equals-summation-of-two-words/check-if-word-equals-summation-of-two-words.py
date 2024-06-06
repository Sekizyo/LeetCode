
import string
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alphabet = list(string.ascii_lowercase)
        first = ""
        second = ""
        target = ""
        for char in firstWord:
            first += str(alphabet.index(char))

        for char in secondWord:
            second += str(alphabet.index(char))

        for char in targetWord:
            target += str(alphabet.index(char))

        if int(first) + int(second) == int(target):
            return True
        return False   