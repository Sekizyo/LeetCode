class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i, num in enumerate(nums2):
            nums1[m+i] = num
        nums1 = nums1.sort()