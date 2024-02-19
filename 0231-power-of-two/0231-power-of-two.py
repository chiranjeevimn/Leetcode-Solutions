class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is positive and has only one set bit
        return n > 0 and (n & (n - 1)) == 0
