# def intervalIntersection(firstList, secondList):
#     l, r = 0, 0
#     result = []

#     while l < len(firstList) and r < len(secondList):
#         a_start, a_end = firstList[l]
#         b_start, b_end = secondList[r]

#         # Find the start and end of the intersection
#         start = max(a_start, b_start)
#         end = min(a_end, b_end)

#         # If there's a valid intersection, add to result
#         if start <= end:
#             result.append([start, end])

#         # Move the pointer for the interval that ends first
#         if a_end <= b_end:
#             l += 1
#         else:
#             r += 1

#     return result




# def canJump(nums):
        
#         l = nums[0]
#         current_index = 0
#         while l < len(nums):
            
#             if l >= len(nums) - 1:
#                 return True
                
#             l += current_index + nums[l]
        
#         return False

# arr = [3,2,1,0,4]

# print(canJump(arr))


# ////////////////////////////////////////////////////////////////

# def printPairs(array): 
#     for i in array:
#         for j in array:
#             print(str(i)+","+str(j))
            

# printPairs([3, 1, 5, 6, 7])


# /////////////////////////////////////////////////////////////


# def printUnorderedPairs(array):
#     for i in range(0,len(array)):
#         for j in range(i+1,len(array)):
#             print(str(array[i]) + "," + str(array[j]))
            

# printUnorderedPairs([3, 1, 5, 6, 7])


# ////////////////////////////////////////////////////////

# o(ab)

# def printUnorderedPairs(arrayA, arrayB):
#     for i in range(len(arrayA)):
#         for j in range(len(arrayB)):
#             if arrayA[i] < arrayB[j]:
#                 print(str(arrayA[i]) + "," + str(arrayB[j]))

# ////////////////////////////////////////////

# def printUnorderedPairs(arrayA, arrayB):
#     for i in range(len(arrayA)):
#         for j in range(len(arrayB)):
#             for k in range(0, 1000):
#                 print(str(arrayA[i]) + "," + str(arrayB[j]))

# 100,000 units of work is still constant 
# Time Complexity : O(ab)

# /////////////////////////////////////////////

my_hashmap = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Get a view of the keys using keys()
keys_view = my_hashmap.keys()

# Convert the view to a list using list()
keys_list = list(keys_view)

print(keys_list)  # Output: ['name', 'age', 'city']



# ////////////////////////////////////////////////////

sample_array = [4, 7]
sample_tuple = tuple(sample_array)

print(f"Converted tuple: {sample_tuple}")  # Output: Converted tuple: (4, 7)



# //////////////////////////////////////////////////
# s = "eat"
# word = s.sort()


# print(word)



def traverse_row_wise(matrix):
  """
  Traverses a matrix row-wise and prints each element.

  Args:
      matrix: A list of lists representing the matrix.
  """
  row = 45
  element = len(matrix[0])
  for row in matrix:
    for element in row:
      print(element, end=" ")  # Print with space separation
    print()  # Move to a new line after each row

# Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
traverse_row_wise(matrix)

# Output:
# 1 2 3 
# 4 5 6 
# 7 8 9 
# arr1 = [4, 2, 7, 10, 6] 
# arr2 = [3]
print(([4, 2, 7, 10, 6] + [3]))
print(([[4, 2, 7, 10, 6]] + [[3]]))






# rows = [[1], [1, 1]]

#         if 1 <= numRows <= 2:
#             return rows[:numRows]

#         for row_index in range(2, numRows):
#             row = [1]

#             for column_index in range(1, row_index):
#                 row.append(rows[-1][column_index - 1] + rows[-1][column_index])
            
#             row.append(1)
#             rows.append(row)

#         return rows
    
    
    
    
    

    
array = ["apple", "banana", "cherry"]
separator = ", "

string = separator.join([str(x) for x in array])

print(string)  # Output: apple, banana, cherry



array = ["apple", "banana", "cherry"]
separator = ", "

# Join the elements with a comma and space separator
string = separator.join(array)

print(string)  # Output: apple, banana, cherry




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1, list2):
    dummy = ListNode()
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
        
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    
    return dummy.next







# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #at he end, slow will be at the center
        if not head or not head.next:
            return

        # Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev, curr = None, slow.next
        slow.next = None  # Split the list into two halves
        while curr:
            next_ = curr.next
            curr.next = prev
            prev, curr = curr, next_

        # Merge the first and the reversed second half
        first, second = head, prev
        while second:
            first.next, first = second, first.next
            second.next, second = first, second.next




class Solution:
    def findDuplicate(self, nums):
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow



        
        