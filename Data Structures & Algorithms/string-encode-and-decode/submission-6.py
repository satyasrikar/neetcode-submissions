class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedStrs = ""
        for _str in strs:
            encodedStrs += "#" + str(len(_str))  + ";" + _str 
        print(encodedStrs)
        return encodedStrs

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                j = i + 1
                while s[j] != ";":
                    j += 1
                # i+1 = start number
                # j = end number
                # s[i+1:j] = number
                wordLen = int(s[i+1:j])
                word = s[j+1: j+1+wordLen]
                res.append(word)
                i = j + 1 + wordLen
            else:
                i += 1
        print(res)
            
            




