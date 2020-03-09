class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //Method
        vector<int> positions {};
        for(int i{};i<nums.size();i++){
            //cout<<nums[i]<<endl;
            for(int j{};j<nums.size();j++){
                if(nums[j] == target - nums[i]){
                    positions.push_back(i);
                    positions.push_back(j);
                    cout<<i<<" - "<<j<<endl;
                    //break;   
                    return positions;
                }
                
            }
        }
        //return nums;
        return positions;
    }
};
