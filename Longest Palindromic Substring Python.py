def longestPalindrome(self, s):
    return s if s == s[::-1] else max(self.longestPalindrome(s[1:]), self.longestPalindrome(s[:-1]), key=len, default="")
