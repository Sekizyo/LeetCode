class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high+1):
            num = str(num)
            if len(num) % 2 == 0:
                left = [int(i) for i in num[:len(num)//2]]
                right = [int(i) for i in num[len(num)//2:]]
                if sum(left) == sum(right):
                    count += 1

        return count
