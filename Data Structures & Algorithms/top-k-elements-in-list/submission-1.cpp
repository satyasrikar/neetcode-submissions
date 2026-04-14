class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
    vector<vector<int>> buckets(nums.size() + 1);
    unordered_map<int, int> freqMap;
    vector<int> result;
    
    //create the freq table 
    for(auto it: nums){
        freqMap[it]++;
    }

    //put freq in buckets
    for(auto &pair: freqMap){
        buckets[pair.second].push_back(pair.first);
    }

    //collect result from bucket (top k)
   for(int i = buckets.size() - 1; i >= 0 && result.size() < k; i--){
    for(auto it: buckets[i]){
        result.push_back(it);
         if (result.size() == k) {
        break;
    }
    }
   }

    return result;
    }
};