class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }
        unordered_map<char, int> sizeList;
        for(char c : s){
            sizeList[c]++;
        }

        for(char c : t){
            sizeList[c]--;
        }

        for(auto p: sizeList){
            if(p.second){
                return false;
            }
        }
        return true;
    }
};
