import sys
class Solution:
    def isHappy(self, n: int) -> bool:
        sys.setrecursionlimit(200)
        sum_ = 0
        for num in list(str(n)):
            sum_ += int(num) ** 2
        
        if sum([int(x) for x in str(sum_)]) == 1:
            return True
        else:
            try:
                return self.isHappy(sum_)
            except Exception as e:
                return False