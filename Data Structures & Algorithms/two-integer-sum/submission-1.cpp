class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> indexMap;

        //build the map
        for(int i = 0; i < nums.size(); i ++){
            indexMap[nums[i]] = i;
        }
        // 1 2 3 4 | 3
        // 1:0 / 2:1 / 3:2 / 4:3

        //check complement and return values
        for(int i = 0; i < nums.size(); i++){
            int complement = target - nums[i];
            if(indexMap.count(complement) && indexMap[complement] != i){
                return {i, indexMap[complement]};
            }
        }
        //return default values

        return {};
    }
};
