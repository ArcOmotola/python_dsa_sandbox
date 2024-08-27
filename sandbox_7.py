nums = [2, 4, 6, 8, 10]

def prefix_sum(arr):
  prefix_arr = [0] * (len(arr) + 1)
  for i in range(1, len(arr) + 1):

      prefix_arr[i] = arr[i - 1] + prefix_arr[i - 1]

      
      
  return prefix_arr
    
print("degugg>>>", prefix_sum(nums))


def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums

print(runningSum(nums))


def pivotIndex(nums):
    total_sum = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i]
        
        if left_sum == right_sum:
            return i
        
        left_sum += nums[i]
    
    return -1  # If no pivot index is found
  
print(pivotIndex([1,7,3,6,5,6]))




class NumArray:
  
  def __init__(self, nums):
    self.prefix_sum = [0] * len(nums)
    for i in range(len(nums)):
      if i > 0:
        self.prefix_sum[i] = nums[i] + self.prefix_sum[i - 1]
      else:
        self.prefix_sum[i] = nums[i]
    
    
  def sumRange(self, left, right):
    return self.prefix_sum[right] - self.prefix_sum[left]
  
  
subArrExample = NumArray([-2, 0, 3, -5, 2, -1])
print(subArrExample.sumRange(1, 4))
    
    





# matrix_arr = [[1, 2, 5], [3, 4, 0], [3, 2, 5]]

# def prefix_sum_matrix(matrix):
#   rows = len(matrix)
#   cols = len(matrix[0])
#   prefix_matrix = [[0] * 3 for _ in range(3)]
#   prev_row = 0
#   sum_seen = 0
  
#   for row in range(rows):
#     for col in range(cols):
      
#       prefix_matrix[row][col] = matrix[row][col]
      

#       if row > prev_row and col == 1:
#         prefix_matrix[row][col] = matrix[row][col] + sum_seen
      
#       if col > 0:
#         prefix_matrix[row][col] = matrix[row][col] + prefix_matrix[row][col - 1]
#         sum_seen = prefix_matrix[row][col]
        
#       prev_row = row

#   return prefix_matrix


# print(prefix_sum_matrix(matrix_arr))



# def computePrefixSum(matrix):
#     if not matrix or not matrix[0]:
#         return []

#     m, n = len(matrix), len(matrix[0])
#     prefix_sum = [[0] * n for _ in range(m)]

#     for i in range(m):
#         for j in range(n):
#             prefix_sum[i][j] = matrix[i][j]

#             if i > 0:
#                 prefix_sum[i][j] += prefix_sum[i-1][j]
#             if j > 0:
#                 prefix_sum[i][j] += prefix_sum[i][j-1]
#             if i > 0 and j > 0:
#                 prefix_sum[i][j] -= prefix_sum[i-1][j-1]

#     return prefix_sum

# matrix_arr = [[1, 2, 5], [3, 4, 0], [3, 2, 5]]

# print(computePrefixSum(matrix_arr))



# nums = [2, 4, 6, 8, 10]

# def prefix_sum(arr):
#   prefix_arr = [0] * len(arr)
#   for i in range(len(arr)):
#     prefix_arr[i] = arr[i] 
#     if i > 0:
#       prefix_arr[i] = arr[i] + prefix_arr[i - 1]
      
#   return prefix_arr
    
    
# print(prefix_sum(nums))

# nums = [2, 4, 6, 8, 10]

# def suffix_sum(arr):
#     suffix_arr = [0] * len(arr)
#     for i in range(len(arr) - 1, -1, -1):
#         suffix_arr[i] = arr[i]
#         if i < len(arr) - 1:
#             suffix_arr[i] = arr[i] * suffix_arr[i + 1]
#     return suffix_arr

# print(suffix_sum(nums))

def subarraySum(nums, k):
  
  l = 0
  count = 0
  
  for i in range(len(nums)):
    
    
    