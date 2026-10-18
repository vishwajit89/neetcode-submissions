class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        S = {}
        T = {}

        for ch in s:
            S[ch] = S.get(ch, 0) + 1

        for ch in t:
            T[ch] = T.get(ch, 0) + 1

        return S == T