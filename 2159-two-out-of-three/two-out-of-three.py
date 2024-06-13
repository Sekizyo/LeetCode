class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)

        output = []
        for num in nums1:
            if num in nums2:
                output.append(num)
            elif num in nums3:
                output.append(num)

        for num in nums2:
            if num in nums1:
                output.append(num)
            elif num in nums3:
                output.append(num)

        for num in nums3:
            if num in nums1:
                output.append(num)
            elif num in nums2:
                output.append(num)

        return set(output)