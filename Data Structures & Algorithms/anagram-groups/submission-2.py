class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)

        for _str in strs:
            strMap["".join(sorted(_str))].append(_str)
        
        result = []

        for _str in strMap.values():
            result.append(_str)

        return result