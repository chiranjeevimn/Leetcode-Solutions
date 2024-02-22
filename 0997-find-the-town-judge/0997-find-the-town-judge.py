class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degrees = [0] * (n + 1)
        out_degrees = [0] * (n + 1)

        for t in trust:
            out_degrees[t[0]] += 1
            in_degrees[t[1]] += 1

        for i in range(1, n + 1):
            if in_degrees[i] == n - 1 and out_degrees[i] == 0:
                return i

        return -1