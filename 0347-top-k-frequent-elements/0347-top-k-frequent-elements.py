class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []


        hm = defaultdict(int)
        freq = []

        for i in range(len(nums)+1):
            freq.append([])

        for i in range(len(nums)):
            hm[nums[i]] = hm[nums[i]]+1
        for key, value in hm.items():
            freq[value].append(key)
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                result.append(num)
            if len(result)==k:
                return result


        
        
        
        


        