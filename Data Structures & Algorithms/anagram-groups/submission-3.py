class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)

        for _str in strs:
            strMap["".join(sorted(_str))].append(_str)
        
        return list(strMap.values())
