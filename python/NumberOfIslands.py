class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j] == '1':
                    islands += 1
                    # Explore from this point, marking everything 2 as we go
                    stack = [(i, j)]
                    while stack:
                        (n, m) = stack.pop()
                        if grid[n][m] == '1':
                            grid[n][m] = '2'
                            if n > 0:
                                stack.append((n-1, m))
                            if n < len(grid)-1:
                                stack.append((n+1, m))
                            if m > 0:
                                stack.append((n, m-1))
                            if m < len(grid[n])-1:
                                stack.append((n, m+1))
        return islands
