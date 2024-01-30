class Solution:
    def reverse(self, x: int) -> int:
        # Initialize the reversed number
        reversed_num = 0
        
        # Determine the sign of the input number
        sign = -1 if x < 0 else 1
        x *= sign  # Make x positive for simplicity
        
        # Reverse the digits of the positive number
        while x:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        # Check for integer overflow
        result = sign * reversed_num
        if result < -2**31 or result > 2**31 - 1:
            return 0  # Return 0 if overflow occurs
        else:
            return result  # Return the reversed number with the original sign
