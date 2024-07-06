# time = "19:34"

# s = "a,b,c"
# print(time.split(':'))  # Output: ['a', 'b', 'c']


# time_str = "19:34"

# # Split the string at the colon (:) and convert each part to an integer
# time_list = [int(part) for part in time_str.split(":")]

# print(time_list)  # Output: [19, 34]

# ////////////////////////////////////////////////////////////////


# time_str = "19:34"

# # Separate digits and convert each to an integer
# time_list = [int(d) for d in time_str if d.isdigit()]

# print(time_list)  # Output: [1, 9, 3, 4]

# import heapq

# arr = [1, 9, 3, 4]
# heapq.heapify(arr)

# heapq.heappop(arr)
# heapq.heappop(arr)
# heapq.heappop(arr)


# print(arr)


# //////////////////////

# arr = [19, 34]

# print(":".join(str(num) for num in arr))


# arr = [1, 9, 3, 4, 9, 10, 3, 3]
arr = [-5, -3, -1, 2, 5, 6, 8]


# def sortedSquares(nums):
#   res = [0] * len(nums)
#   l = 0
#   r = len(nums) - 1
  
#   for i in range(len(nums) - 1, -1, -1):
#     if abs(nums[l]) > abs(nums[r]):
#       val = nums[l]
#       l += 1
#     else:
#       val = nums[r]
#       r -= 1
      
#     res[i] = val ** 2
    
    
#   return res

# print(sortedSquares(arr))



input = "A man, a plan, a canal: Panama"

print(input.split(" "))

"amanaplanacanalpanama"

word="R9eP"
print(word.lower())


def split_sentence(sentence):


  words = []
  current_word = ""
  for char in sentence:
    if char.isspace():
      # Whitespace encountered, add current word and reset
      words.append(current_word)
      current_word = ""
    else:
      # Append current character to the word
      current_word += char
  # Add the remaining word after the loop
  if current_word:
    words.append(current_word)
  return words

sentence = "the sky is blue"
words = split_sentence(sentence)
print(words)  # Output: ["the", "sky", "is", "blue"]



def spiralOrder(matrix):
  res = []
  left = 0
  right = len(matrix[0])
  top = 0
  bottom = len(matrix)
  
  while left < right and top < bottom:
    # traverse top
    for i in range(left, right):
      res.append(matrix[top][i])
    top += 1
    
    # traverse right
    for i in range(top, bottom):
      res.append(matrix[i][right-1])
      
    right -= 1
    
    if not (left < right and top < bottom):
      break
    
    # traverse bottom
    for i in range(right - 1, left - 1, -1):
      res.append(matrix[bottom - 1][i])
      
    bottom -= 1
    
    # traverse left
    for i in range(bottom - 1, top - 1, -1):
      res.append(matrix[i][left])

    left += 1
      
    
    ### traverse (left, right, top, bottom)
    
    
    
  return res
  
  
sudoku = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
  
print(spiralOrder(sudoku))


t = "onomatopoeia"

print("tester>>>", t[2:5])

seeking = set([char for char in t])

print(seeking)