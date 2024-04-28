class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        output = []
        maxA = numbers.index(max(numbers))
        if maxA < len(numbers)-1:
            maxB = numbers.index(max(numbers), maxA+1)
            if numbers[maxA] + numbers[maxB] == target:
                return [maxA+1, maxB+1]

        for i, num1 in enumerate(numbers):
            for num2 in numbers[i+1:]:
                if num1 + num2 == target:
                    return [i+1, numbers.index(num2, i+1)+1]

        return output