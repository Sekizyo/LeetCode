class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum0 = 0

        splitted = list(str(n))
        for num in splitted:
            num = int(num)
            product *= num
            sum0 += num

        return product - sum0 
        