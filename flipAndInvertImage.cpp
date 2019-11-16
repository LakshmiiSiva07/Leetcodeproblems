/*Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0]*/
class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
   int temp = 0;
   for (auto i = 0; i < A.size(); i++)
	{
        int size = (A[i].size() - 1);
        int mid_size = A[i].size()/ 2;
		
		for (auto j = 0; j < mid_size; j++)
		{
			temp = A[i][j];
			A[i][j] = (1 - (A[i][size - j]));
			A[i][size - j] = (1 - temp);
		}
        if ((A[i].size()%2 != 0))
            A[i][mid_size] = 1 - A[i][mid_size];
	}
        
     return A;
    }
   
};
