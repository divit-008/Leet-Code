class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = nums1+nums2
        n.sort()
        x = len(n) % 2
        # [1, 2, 3, 4, 5, 6] 

        return n[int(len(n)/2)] if x == 1 else (n[int(len(n)/2)]+n[int((len(n)/2)-1)])/2