class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = 0
        even = 0
        
        for x in position:
            if x%2:
                odd = odd + 1
            else:
                even = even + 1
        if odd > even :
            return even
        else :
            return odd
