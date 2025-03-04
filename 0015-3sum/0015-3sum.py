class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            nl,r = i+1, len(nums)-1
            while nl<r:
                val = nums[i]+nums[nl]+nums[r]
                if val == 0:
                    ans.add((nums[i], nums[nl], nums[r]))
                    nl+=1
                    r-=1
                elif val<0:
                    nl+=1
                elif val>0:
                    r-=1
        return list(ans)
        

            


        