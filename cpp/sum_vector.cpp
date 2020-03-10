#include <iostream>
#include <vector>
#include <map>

using namespace std;
class Solution {
    public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> positions {};
        map<int, int> hashTable{};
        for(int i{};i<nums.size();i++){ 
            cout<<"KEY: "<<nums[i]<<" - VALUE: "<<i<<endl;
            hashTable.insert({nums[i],i});
        }
        for(int j{};j<nums.size();j++){
            int complement = target - nums[j];
            if(hashTable.count(complement) && hashTable.at(complement) != j){
                positions.push_back(j);
                positions.push_back(hashTable.at(complement));
                cout<<j<<" - "<<hashTable.at(complement)<<endl;
                return positions;
            }
        }
        return positions;
    }
    vector<int> twoSum2(vector<int>& nums, int target) {
        vector<int> positions {};
        for(int i{};i<nums.size();i++){
            //cout<<nums[i]<<endl;
            for(int j{};j<nums.size();j++){
                if(nums[j] == target - nums[i]){
                    positions.push_back(i);
                    positions.push_back(j);
                    cout<<i<<" - "<<j<<endl;
                    return positions;
                }                
            }
        }
        return positions;
    }
};


int main(){
    cout<<"<< Sum of two numbers >>"<<endl;
    Solution s1;
    vector<int> in_test = {1,3,5,6,2,7,9,13,8};
    s1.twoSum(in_test,11);
    s1.twoSum2(in_test,11);




    return 0;
}