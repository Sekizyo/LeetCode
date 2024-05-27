class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_ = 0
        for num in list(str(x)):
            sum_ += int(num)

        if x % sum_ == 0:
            return sum_
        else:
            return -1
        