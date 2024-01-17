class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        occurens = set()

        for value in count.values():
            if value in occurens:
                return False
            occurens.add(value)

        return True