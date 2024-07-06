arr = [[1,40,3,10],[4,5,6,20],[7,8,9,30]]

# Row-wise Traversal

def traverse_row_wise(matrix):
  for row in range(len(matrix)):
    for col in range(len(matrix[row])):
      print(matrix[row][col])
      
traverse_row_wise(arr)

# Column-wise Traversal

# ////////////////////////////////////////////////////////////////

# def traverse_column_wise(matrix):
#     rows, cols = len(matrix), len(matrix[0])
#     for col in range(cols):
#         for row in range(rows):
#             print(matrix[row][col], end=' ')
#         print()  # for a new line after each column

# traverse_column_wise(arr)


# def traverse_column_wise(matrix):
#     # rows, cols = len(matrix), len(matrix[0])
#     for col in range(len(matrix[0])):
#         for row in range(len(matrix)):
#             print(matrix[row][col], end=' ')
#         print()  # for a new line after each column

# traverse_column_wise(arr)



# ////////////////////////////////////////////////////////

# Diagonal Traversal

def traverse_diagonal(matrix):
    rows, cols = len(matrix), len(matrix[0])
    for line in range(1, (rows + cols)):
        start_col = max(0, line - rows)
        count = min(line, (cols - start_col), rows)
        for j in range(0, count):
            print(matrix[min(rows, line) - j - 1][start_col + j], end=' ')
        print()  # for a new line after each diagonal

traverse_diagonal(arr)



# //////////////////////////////////////////////////////


# Zigzag (Snake) Traversal

# def traverse_zigzag(matrix):
#     if not matrix or not matrix[0]:
#         return
#     rows, cols = len(matrix), len(matrix[0])
#     for row in range(rows):
#         if row % 2 == 0:
#             for col in range(cols):
#                 print(matrix[row][col], end=' ')
#         else:
#             for col in range(cols - 1, -1, -1):
#                 print(matrix[row][col], end=' ')
#         print()  # for a new line after each row
        
        
# //////////////////////////////////////////////////////

# Spiral Traversal

# def traverse_spiral(matrix):
#     if not matrix:
#         return
#     top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
#     while top <= bottom and left <= right:
#         for i in range(left, right + 1):
#             print(matrix[top][i], end=' ')
#         top += 1
#         for i in range(top, bottom + 1):
#             print(matrix[i][right], end=' ')
#         right -= 1
#         if top <= bottom:
#             for i in range(right, left - 1, -1):
#                 print(matrix[bottom][i], end=' ')
#             bottom -= 1
#         if left <= right:
#             for i in range(bottom, top - 1, -1):
#                 print(matrix[i][left], end=' ')
#             left += 1
#         print()  # for a new line between each loop

# ////////////////////////////////////////////////////////////////////////////
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Accessing row data
# row_1 = matrix[0]  # Accesses the first row (list [1, 2, 3])

# # Accessing column data (requires iterating over rows)
# column_2 = []
# for row in matrix:
#   column_2.append(row[1])  # Append the second element (index 1) from each row

# print(row_1)  # Output: [1, 2, 3]
# print(column_2)  # Output: [2, 5, 8]


print(" 7383".isalnum())

vowels = "aeiou"
vowels += vowels.upper()
print(vowels)


def threeSum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums)):
        
        l = i + 1
        r = len(nums) - 1
        while l < r:
            sum_total = nums[i] + nums[l] + nums[r]
            if sum_total > 0:
                r -= 1
            elif sum_total < 0:
                l += 1
            else:
                result.append([nums[i], nums[l], nums[r]])
    return result


print(threeSum([-1,0,1,2,-1,-4]))