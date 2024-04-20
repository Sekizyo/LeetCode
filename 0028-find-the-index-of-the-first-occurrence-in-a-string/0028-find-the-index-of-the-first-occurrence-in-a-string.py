class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0

        output = -1
        needle = list(needle)
        for i in range(len(haystack)-len(needle)+1):
            j = 0
            for char in needle:
                if char == haystack[i+j]:
                    j += 1
                else:
                    break

                if j == len(needle):
                    return i
        return output
        