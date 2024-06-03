class Solution:
    def replaceDigits(self, s: str) -> str:
        output = ""
        for i in range(0, len(s)-1, 2):
            letter = s[i]
            num = s[i+1]
            output += letter
            output += chr(ord(letter) + int(num))
        
        if (len(s)-1) % 2 == 0:
            output += s[-1]

        return output