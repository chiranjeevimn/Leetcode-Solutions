class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF

        while b != 0:
            # Calculate sum without carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # If the result is a positive number, return it directly
        # If it's a negative number, convert it to a 32-bit integer representation
        return a if a <= MAX else ~(a ^ mask)