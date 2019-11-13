/*
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition
*/

class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        vector <int> v;
		for (auto i = A.begin(); i != A.end(); ++i) {
			if (((*i) % 2) == 0)
				v.emplace(v.begin(),*i);
			else
				v.push_back(*i);
        }
		return v;
	}
};
