class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(s) - 1

        while j >= 0 and s[j] == ' ':
            j -= 1
        last = j
        while j >= 0 and s[j] != ' ':
            j -= 1

        return last - j