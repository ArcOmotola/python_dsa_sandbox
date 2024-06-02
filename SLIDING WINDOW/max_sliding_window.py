



















# def max_sliding_window_two_pointers(nums, k):
#   l = 0
#   r = 0
#   max_arr = []
#   current_max = float("-inf")

#   while r < len(nums):
#     current_max = max(current_max, nums[r])
    
#     if r - l + 1 == k:
#       max_arr.append(current_max)

#       if nums[l] == current_max:
#         current_max = max(nums[l+1:r+1])
      
#       l += 1

#     r += 1
  
#   return max_arr



# # Sample array and window size
# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3

# # Apply the two-pointer sliding window algorithm
# result = max_sliding_window_two_pointers(nums, k)
# print("Max values in each window:", result)






# def max_sliding_window(nums, k):
#     # This will hold the maximum values for each window
#     max_values = []
#     # We use a deque to store the indices of elements
#     from collections import deque
#     q = deque()
    
#     for i in range(len(nums)):
#         # Remove elements not within the window
#         if q and q[0] < i - k + 1:
#             q.popleft()
        
#         # Maintain the decreasing order in deque
#         while q and nums[q[-1]] < nums[i]:
#             q.pop()
        
#         # Add the current element at the end of the deque
#         q.append(i)
        
#         # The first element is the largest one in the window
#         if i >= k - 1:
#             max_values.append(nums[q[0]])
    
#     return max_values

# # Sample array and window size
# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3

# # Apply the sliding window algorithm
# result = max_sliding_window(nums, k)
# print("Max values in each window:", result)
