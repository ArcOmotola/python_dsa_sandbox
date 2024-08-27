def numIslands(grid):
  if not grid:
    return 0
  
  m = len(grid)
  n = len(grid)
  
  island_count = 0
  
  def dfs(x, y):
    if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == "0":
      return
    
    grid[x][y] = "0"
    
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x,y+1)
    dfs(x,y-1)
    
  for i in range(m):
    for j in range(n):
      if grid[i][j] == "1":
        island_count += 1
        dfs(i, j)
        


  return island_count
        