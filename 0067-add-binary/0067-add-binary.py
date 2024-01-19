class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize an empty list to store the result
        ans = []
        
        # Initialize the carry to 0
        carry = 0
        
        # Initialize pointers for the two input strings
        i = len(a) - 1
        j = len(b) - 1

        # Iterate through the strings and the carry
        while i >= 0 or j >= 0 or carry:
            # Add the current digit from string 'a' to the carry if it exists
            if i >= 0:
                carry += int(a[i])
                i -= 1

            # Add the current digit from string 'b' to the carry if it exists
            if j >= 0:
                carry += int(b[j])
                j -= 1

            # Append the remainder of the carry (either 0 or 1) to the result list
            ans.append(str(carry % 2))
            
            # Update the carry for the next iteration
            carry //= 2

        # Return the result as a string, reversed and joined
        return ''.join(ans[::-1])
