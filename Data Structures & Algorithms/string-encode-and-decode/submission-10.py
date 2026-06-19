class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for _str in strs:
            encodedStr += "#" + str(len(_str)) + "$" + _str
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedStrs = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                j = i + 1
                while s[j] != "$":
                    j += 1
                wordLen = int(s[i+1: j])
                word = s[j+1: j+1+wordLen]
                decodedStrs.append(word)
                i = j + 1 + wordLen
            else:
                i += 1
        return decodedStrs
                

