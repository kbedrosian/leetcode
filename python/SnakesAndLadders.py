class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        boardList = []
        for i, row in enumerate(board[::-1]):
            if i % 2 == 1:
                row = row[::-1]
            boardList += row

        positions = range(len(boardList))
        distances = {}
        for pos in positions:
            distances[pos] = float('inf')
        distances[0] = 0

        unvisited = set(positions)
        currPos = 0
        while True:
            unvisited.remove(currPos)
            # Go through neighbors of curr
            for newPos in range(currPos+1, min(currPos+7, len(boardList))):
                if boardList[newPos] != -1:
                    newPos = boardList[newPos]-1
                newDist = min(distances[newPos], distances[currPos]+1)
                distances[newPos] = newDist
            if not unvisited:
                break
            minUnvisited = None
            minDist = float('inf')
            for unvisitedPos in unvisited:
                if distances[unvisitedPos] < minDist:
                    minDist = distances[unvisitedPos]
                    minUnvisited = unvisitedPos
            if minUnvisited is None:
                break
            currPos = minUnvisited

        result = distances[len(boardList)-1]
        if result == float('inf'):
            result = -1
        return result


