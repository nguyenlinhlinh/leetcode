# https://leetcode.com/problems/shortest-bridge/
class Solution:
    def findIsland(self, grid, path, visited, stack):
        result = []
        n = len(grid)
        while stack:
            (r, c) = stack.pop()
            if grid[r][c] == 1:
                result.append((r, c))
                if not visited[r][c]:
                    visited[r][c] = True
                    if c + 1 < n:
                        stack.append((r, c + 1))
                    if r + 1 < n:
                        stack.append((r + 1, c))
            else:
                if not visited[r][c]:
                    visited[r][c] = True
                    path.append((r, c))
        return result, r, c
            

    def shortestBridge(self, grid):
        islands = []
        n = len(grid)
        visited = [[False for i in range(0, n)] for i in range(0, n)]
        path = []
        
        r = 0
        c = 0
        for r in range(0, n):
            for c in range(0, n):
                if grid[r][c] == 0 and not visited[r][c]:
                    path.append((r,c))
                    visited[r][c] = True
                else:
                    if not visited[r][c]:
                        island, r, c = self.findIsland(grid, path, visited, [(r, c)])
                        islands.append(island)

# test cases 
one = [[0,1],[1,0]]
two = [[0,1,0],[0,0,0],[0,0,1]]
three = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
s = Solution()
s.shortestBridge(three)