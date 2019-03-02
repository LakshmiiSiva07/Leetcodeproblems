import copy
class Solution(object):
    def orangesRotting(self, grid):
        """
       In a given grid, each cell can have one of three values:
       the value 0 representing an empty cell;
       the value 1 representing a fresh orange;
       the value 2 representing a rotten orange.
       Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
       Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
        :type grid: List[List[int]]
        :rtype: int
        """
        minutes = 0
        no_fresh_oranges = 0
        old_fresh_oranges = 0
        grid_copy = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == 1):
                    no_fresh_oranges = no_fresh_oranges + 1
        if(no_fresh_oranges == 0):
            return minutes
        else:
             old_fresh_oranges = 0
             grid_copy = copy.deepcopy((grid))
             while(no_fresh_oranges > 0 and old_fresh_oranges != no_fresh_oranges):
                    old_fresh_oranges = no_fresh_oranges
                    for i in range(len(grid)):
                        for j in range(len(grid[i])):
                            if(grid_copy[i][j] == 2):
                                if(grid[i - 1][j] == 1 and i > 0):
                                    grid[i -1][j] = 2
                                    no_fresh_oranges = no_fresh_oranges - 1
                                if( i < (len(grid) - 1) and grid[i + 1][j] == 1):
                                    grid[i + 1][j] = 2
                                    no_fresh_oranges = no_fresh_oranges - 1
                                if (grid[i][j - 1] == 1 and j > 0):
                                    grid[i][j - 1] = 2
                                    no_fresh_oranges = no_fresh_oranges - 1
                                if(j < (len(grid[i]) - 1) and grid[i][j + 1] == 1 ):
                                    no_fresh_oranges = no_fresh_oranges - 1
                                    grid[i][j + 1] = 2
                    grid_copy = copy.deepcopy(grid)
                    minutes = minutes + 1
        if(no_fresh_oranges > 0):
            return  -1
        return minutes
