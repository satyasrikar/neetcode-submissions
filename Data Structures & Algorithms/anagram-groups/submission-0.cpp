class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
         vector<vector<string>> ans;
        unordered_map<string, vector<string>> umap;


        for(auto iterator: strs){
            string originalString = iterator;
            sort(iterator.begin(), iterator.end());
            umap[iterator].push_back(originalString);
        }

        for(auto it: umap){
            ans.push_back(it.second);
        }

        return ans;
    }
};
