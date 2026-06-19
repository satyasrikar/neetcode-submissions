class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = defaultdict(int)

        for c in s:
            countS[c] += 1

        for c in t:
            countS[c] -= 1

        for c in countS:
            if countS[c] != 0:
                return False

        return True
