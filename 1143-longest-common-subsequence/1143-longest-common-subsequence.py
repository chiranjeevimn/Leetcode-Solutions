class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # Initialize a 2D array to store the lengths of LCS
        o = [[0] * (n + 1) for _ in range(m + 1)]

        # Build the o array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    o[i][j] = 1 + o[i - 1][j - 1]
                else:
                    o[i][j] = max(o[i - 1][j], o[i][j - 1])

        return o[m][n]


