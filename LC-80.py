class Solution(object):
    def removeDuplicates(self, nums):
        if not nums: 
            return 0
        l = 1 # Left Pointer
        count = 1
        n = len(nums)
        
        # iterating r
        for r in range(1, n):
            if nums[r] == nums[r-1]:
                count += 1
            else:
                count = 1
        
            if count <= 2:
                nums[l] = nums[r]
                l += 1
        
        return l 

        # Time Complexity = O(n)
        # Space Complexity = O(1)
        # Variable Sliding Window Concept

        
