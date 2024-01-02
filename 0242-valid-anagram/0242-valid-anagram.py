class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if lengths are different
        if len(s) != len(t):
            return False

        # Create dictionaries to store character counts
        count_s = {}
        count_t = {}

        # Populate count_s dictionary
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        # Populate count_t dictionary
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # Compare the dictionaries
        return count_s == count_t
