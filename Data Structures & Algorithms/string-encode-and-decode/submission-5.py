class Solution:

    def encode(self, strs):
        encodedString = ""
        for str in strs:
            encodedString = encodedString + len(str).__str__() + '#' + str
        return encodedString


    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            if(j == -1):
                break
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            i = j + 1 + length

        return res
