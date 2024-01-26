class Solution:
    def mySqrt(self, x: int) -> int:
        return bisect.bisect_right(range(x + 1), x, key=lambda b: b * b) - 1