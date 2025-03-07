from math import sqrt
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime  = []
        for _ in range(right+1):
            prime.append(True)
        for i in range(2, math.ceil(math.sqrt(right))+1):
            if prime[i]:
                k = 2
                while i*k <= right:
                    prime[i*k] = False
                    k+=1
        l = max(left, 2)
        while l<right and not prime[l]:
            l+=1
        r = l+1

        mn = [float('inf'), float('inf')]
        while r<=right:
            while r<=right and not prime[r]:
                r+=1
            if r>right:
                break
            if mn[0] == float('inf'):
                mn = [l,r]
            else : 
                cmd , nd = mn[1]-mn[0], r-l

                if nd < cmd:
                    mn = [l, r]
            
            l = r
            r+=1
        
        return mn if mn[0] != float('inf') else [-1, -1]


        