class Solution:
    
    def romanToInt(self, s: str) -> int:
        number = 0
        ROMANS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i, char in enumerate(s[:-1]):
            if ROMANS[s[i + 1]] > ROMANS[char]:
                number -= ROMANS[char]
            else:
                number += ROMANS[char]

        number += ROMANS[s[-1]]
        
        return number
