/*Identify if duplicates are present */
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        sort(nums.begin(), nums.begin()+nums.size());
		for (auto i = 1; i < nums.size(); i++)
		{
			if (nums[i] == nums[i - 1])
				return true;
		}
		return false;
        
    }
};
