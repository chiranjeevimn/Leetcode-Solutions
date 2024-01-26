class Solution:
    def isValid(self, s: str) -> bool:
        a = []

        for c in s:
            if c == '(':
                a.append(')')
            elif c == '{':
                a.append('}')
            elif c == '[':
                a.append(']')
            elif not a or a.pop() != c:
                return False

        return not a