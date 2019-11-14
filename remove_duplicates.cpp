/*Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.*/

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
		for (auto i = 1; i < nums.size(); i++)
		{
			while((nums.size() > 1)  && (i < nums.size()) && nums[i] == nums[i - 1])
				nums.erase(nums.begin()+i);
		}
		return nums.size();
        
    }
}
