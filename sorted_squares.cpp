/*Given an array of integers A sorted in non-decreasing order,
return an array of the squares of each number, also in sorted non-decreasing order.*/
class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        
    	for (auto i = 0; i < A.size(); i++)
		{
			A[i] = A[i] * A[i];
		}
		sort(A.begin(), A.begin()+A.size());
		return A;
        
    }
};
