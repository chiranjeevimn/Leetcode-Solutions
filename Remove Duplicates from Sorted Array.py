class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        
        cur = 0
        for next in range(1, len(nums)):
            if nums[next] != nums[cur] :
                cur += 1
                nums[cur] = nums[next];            
        
        return cur + 1