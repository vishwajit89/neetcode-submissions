class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s = {}
        p = {}
        for ch  in ransomNote:
            s[ch] = s.get(ch,0)+1
        for ch in magazine:
            p[ch] = p.get(ch,0)+1
        for ch  in ransomNote:
            if s[ch]>p.get(ch,0):
                return False
        return True