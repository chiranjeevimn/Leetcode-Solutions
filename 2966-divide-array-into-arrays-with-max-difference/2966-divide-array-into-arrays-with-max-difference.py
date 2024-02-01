class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        a = []

        nums.sort()

        for i in range(2, len(nums), 3):
            if nums[i] - nums[i - 2] > k:
                return []
            a.append([nums[i - 2], nums[i - 1], nums[i]])

        return a