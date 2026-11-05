class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(nums)<2):
            return False
        for i in range(len(nums)-1):
            x=nums[i]
            for j in range(i+1,len(nums)):
                if(x==nums[j]):
                    return True
        return False
