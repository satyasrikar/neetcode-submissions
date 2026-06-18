class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for _string in strs:
            encodedString += "#" + str(len(_string)) + "$" + _string
        
        return encodedString

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                j = i + 1
                while s[j] != "$":
                    j += 1
                wordLen = int(s[i+1: j])
                word = s[j+1 : j+1+wordLen]
                res.append(word)
                i = j+1+wordLen
            else:
                i += 1
        return res

