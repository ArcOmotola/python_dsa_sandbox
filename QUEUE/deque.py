from collections import deque

dq = deque([1, 2, 3])
dq.extend([4, 5])
print(dq)  # Output: deque([1, 2, 3, 4, 5])



arr1 = [3, 5, 2, 5, 9]
arr2 = [9, 8, 10]

arr3 = arr2 + arr1

print("array>>", arr3)


print(arr1.count(5))





# def rotate_array(arr, n):
#   """
#   Rotates an array by a given number of positions (n) to the right.

#   Args:
#       arr: The array to be rotated.
#       n: The number of positions to rotate by (positive integer).

#   Returns:
#       The rotated array.
#   """
#   n = n % len(arr)  # Handle rotations larger than array size
#   # Reverse the entire array first
#   arr.reverse()
#   # Reverse the first n elements (new beginning)
#   first_part = arr[:n]
#   first_part.reverse()
#   # Reverse the remaining elements (new end)
#   remaining_part = arr[n:]
#   remaining_part.reverse()
#   # Combine the reversed parts
#   arr[:] = first_part + remaining_part
#   return arr

# # Example usage
# my_array = [1, 2, 3, 4, 5]
# rotated_array = rotate_array(my_array.copy(), 2)  # Avoid modifying original array
# print(rotated_array)  # Output: [4, 5, 1, 2, 3]
