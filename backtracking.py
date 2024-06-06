# def backtrack(path, choices):
#   if is_solution(path):
#     output(path)
#     return
  
#   for choice in choices:
#     if is_valid(choice, path):
#       path.append(choice)
#       backtrack(path, choices)
#       path.pop() # Undo the current choice (backtrack)

def solve_n_queens(n):
  def backtrack(row, path):
    if row == n:
      results.append(path.copy())
      return
    
    for col in range(n):
      if col in columns or (row - col) in diag1 or (row + col) in diag2:
        continue # Skip the attacked areas
      
      columns.add(col)
      diag1.add(row - col)
      diag2.add(row + col)
      path.append(col)
      
      backtrack(row + 1, path)
      
      columns.remove(col)
      diag1.remove(row - col)
      diag2.remove(row + col)
      path.pop()
      
      
  
  results = []
  columns = set()
  diag1 = set()
  diag2 = set()
  backtrack(0, [])
  return results
  
  
  
# To use it
n = 4
print(solve_n_queens(n))