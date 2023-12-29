class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        if not nums1 or not nums2:
            return []

        ans = collections.Counter(nums1)

        res = []

        for i in nums2:
            if i in ans and ans[i]:
                res.append(i)
                ans[i] -= 1
            
        return res
                