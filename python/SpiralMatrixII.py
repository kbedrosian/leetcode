class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        m = [[0]*n for _ in xrange(n)]
        currRow = 0
        currCol = 0
        currSideLen = n
        val = 1
        while currSideLen > 1:
            # Populate the top edge, from left to right
            for j in range(currSideLen):
                m[currRow][currCol+j] = val
                val += 1
            # Populate the right edge, from top to bottom
            for i in range(1, currSideLen):
                m[currRow+i][currCol+currSideLen-1] = val
                val += 1
            # Populate the bottom edge, from right to left
            for j in reversed(range(currSideLen-1)):
                m[currRow+currSideLen-1][currCol+j] = val
                val += 1
            # Populate the left edge, from bottom to top
            for i in reversed(range(1, currSideLen-1)):
                m[currRow+i][currCol] = val
                val += 1
            currSideLen -= 2
            currRow += 1
            currCol += 1
        if currSideLen == 1:
            m[currRow][currCol] = val
        return m

