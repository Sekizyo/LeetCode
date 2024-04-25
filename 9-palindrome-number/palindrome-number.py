class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = list(str(x))
        y.reverse()

        if list(str(x)) == y:
            return True
        return False