class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of each element
            frequency_counter = Counter(nums)

            # Sort the array based on frequency and value
            nums.sort(key=lambda x: (frequency_counter[x], -x))

            return nums