class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        q = collections.deque([num for num in range(1, 10)])

        while q:
            num = q.popleft()
            if num > high:
                return ans
            if low <= num <= high:
                ans.append(num)
            
            lastDigit = num % 10
            if lastDigit < 9:
                q.append(num * 10 + lastDigit + 1)

        return ans