def print_matrix_backwards(matrix):
    # Get the number of rows and columns
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    # Traverse the matrix from the last row to the first row
    for c in range(cols):
        # Traverse each row from the last element to the first element
        for r in range(rows):
            print(matrix[r][c], end=' ')
        print()  # Newline after each row

# Example matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Print the matrix backwards
print_matrix_backwards(matrix)



# whats the difference between 

count = {}

for r in range(len(s)):
  if s[r] not in count:
    count[s[r]] = 1
  else:
    count[s[r]] += 1
    

count = {i:s.count(i) for i in range(s)}

for r in range(len(s)):
  count[s[r]] = 1 + count.get(s[r], 0)
  


