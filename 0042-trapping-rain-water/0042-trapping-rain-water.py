class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l,r = 0 , len(height)-1
        lh, rh = height[l], height[r]

        while l<r :
            if lh<=rh:
                l+=1
                lh = max(lh, height[l])
                water += (lh-height[l])
            else:
                r-=1
                rh = max(rh, height[r])
                water+=(rh-height[r])
        return water






        